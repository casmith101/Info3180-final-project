<template>
    <div class="registrationForm"> 
        <form id="userForm" @submit.prevent="registerUser">

            <div class="form-group">
                <div class="input-group">
                    <label for="username" class ="form-label"> Username </label>
                    <input type="text" id="username" name="username" v-model="user.username" class="form-control"/>
                </div>

                <div class="input-group">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" id="password" name="password" v-model="user.password" class="form-control">
                </div>
            </div>

            <div class="form-group">
                <div class="input-group">
                    <label for="firstname" class="form-label">First name</label>
                    <input type="text" id="firstname" name="firstname" v-model="user.firstname" class="form-control">
                </div>

                <div class="input-group">
                    <label for="lastname" class="form-label">Last name</label>
                    <input type="text" id="lastname" name="lastname" v-model="user.lastname" class="form-control">
                </div>
            </div>

            <div class="form-group">
                <div class="input-group">
                    <label for="email" class="form-label">Email</label>
                    <input type="text" id="email" name="email" v-model="user.email" class="form-control">
                </div>

                <div class="input-group">
                    <label for="location" class="form-label">Location</label>
                    <input type="text" id="location" name="location" v-model="user.location" class="form-control">
                </div>
            </div>

            <div class="input-group textarea">
                <label for="bio" class="form-label">Bio</label>
                <textarea id="bio" name="biography" v-model="user.biography" class="form-control"></textarea>
            </div>

            <div class="form-photo">
                <label for="photo" class="form-label">Profile Photo</label>
                <input type="file" ref="profile_photo" id="photo" name="profile_photo" class="form-control">
            </div>

        <button type="submit">Register</button>
        </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const user = ref({
    username: "",
    password: "",
    firstname: "",
    lastname: "",
    email: "",
    location: "",
    biography: "",
    profile_photo: null
});

let csrf_token = ref(""); 

function getCsrfToken() { 
    fetch('/api/v1/csrf-token') 
    .then((response) => response.json()) 
    .then((data) => { 
        console.log(data); // Log the CSRF token data
        csrf_token.value = data.csrf_token; 
        console.log(csrf_token.value); // Log the CSRF token value
    }) 
}

const registerUser = () => {
    let userForm = document.getElementById('userForm');
    let form_data = new FormData(userForm);

    fetch("/api/v1/register", {
        method: 'POST',
        body: form_data,
        headers: { 
            'X-CSRFToken': csrf_token.value 
        }
    })
    .then(function (response) { 
        
        return response.json(); 
    }) 
    .then(function (data) { 
        // display a success message 
        console.log(data); 
    }) 
    .catch(function (error) { 
        console.log(error); 
    });
}

onMounted(() => { 
    getCsrfToken(); 
}); 
</script>
