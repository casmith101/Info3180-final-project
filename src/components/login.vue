<template>
    <div class="Login"> 
        <form id="login" @submit.prevent="Login">

            <div class="form-group">
                <div class="input-group">
                    <label for="username" class ="form-label"> Username </label>
                    <input type="text" id="username" name="username" v-model="login.username" class="form-control"/>
                </div>

                <div class="input-group">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" id="password" name="password" v-model="login.password" class="form-control">
                </div>
            </div>

            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

const login = ref({
    username: "",
    password: ""
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
    let login = document.getElementById('login');
    let form_data = new FormData(login);

    fetch("/api/v1/auth/login", {
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