"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""



import datetime
from app import app, db
from app.forms import RegistrationForm, LoginForm, PostForm
from flask import render_template, request, jsonify, send_file
from app.models import User, Post, Follow
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import SQLAlchemyError
from flask_wtf.csrf import generate_csrf
import os


###
# Routing for your application.
###

@app.route('/api/v1/register', methods=['POST'])
def add_user():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data  
        email = form.email.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        location = form.location.data
        biography = form.biography.data
        profile_photo = request.files['profile_photo']
        filename = secure_filename(profile_photo.filename)
        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        new_user = User(
            username=username,
            password=password,  
            firstname=firstname,
            lastname=lastname,
            email=email,
            location=location,
            biography=biography,
            profile_photo=filename
        )

        db.session.add(new_user)
        db.session.commit()

        response = {
            'message': 'user Successfully added',
            'username': new_user.username,
            'email': new_user.email,
            'firstname': new_user.firstname,
            'lastname': new_user.lastname,
            'location': new_user.location,
            'biography': new_user.biography,
            'profile_photo': filename
        }

        return jsonify(response), 200
    else:
        errors = form.errors
        return jsonify({'errors': errors}), 400

    
@app.route('/api/v1/csrf-token', methods=['GET']) 
def get_csrf(): 
    return jsonify({'csrf_token': generate_csrf()})  


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/api/v1/auth/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/api/v1/users/<int:user_id>/posts', methods=['POST'])
@login_required
def add_post(user_id):
    if user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json()
    post = Post(caption=data['caption'], photo=data['photo'], user_id=user_id, created_on=datetime.datetime.now())
    db.session.add(post)
    db.session.commit()
    return jsonify({"message": "Post added successfully"}), 201

@app.route('/api/v1/users/<int:user_id>/posts', methods=['GET'])
def get_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    return jsonify([{"caption": post.caption, "photo": post.photo, "created_on": post.created_on} for post in posts]), 200

@app.route('/api/users/<int:user_id>/follow', methods=['POST'])
@login_required
def follow_user(user_id):
    if current_user.id == user_id:
        return jsonify({"error": "Cannot follow yourself"}), 400
    follow = Follow(follower_id=current_user.id, user_id=user_id)
    db.session.add(follow)
    db.session.commit()
    return jsonify({"message": "Followed successfully"}), 201

@app.route('/api/v1/posts', methods=['GET'])
def all_posts():
    posts = Post.query.all()
    return jsonify([{"user_id": post.user_id, "caption": post.caption, "photo": post.photo, "created_on": post.created_on} for post in posts]), 200

##
# The functions below should be applicable to all Flask apps.
##

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404