<template>
    <div class="PostForm"> 
        <form id="postForm" @submit.prevent="NewPost">

            <div class="form-photo">
                <label for="photo" class="form-label">New Photo</label>
                <input type="file" ref="profile_photo" id="photo" name="profile_photo" class="form-control">
            </div>

            <div class="input-group">
                <label for="caption" class="form-label">Caption</label>
                <textarea id="caption" name="caption" v-model="post.caption" class="form-control"></textarea>
            </div>

            <button type="submit">SUBMIT</button>
        </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const post = ref({
    caption: "",
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
    let post = document.getElementById('postForm');
    let form_data = new FormData(post);

    fetch("/api/v1/users/<int:user_id>/posts", {
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