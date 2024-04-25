<script>
    import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
    <main>
        <header class="header">
            <nav>
                <div class="logo">
                    <a href="/">
                        <img alt="Vue logo" class="logo-image" src="./assets/logo.png" />
                        <span>Photogram</span>
                    </a>
                </div>
                
                <ul class="menu">
                    <RouterLink to="/">Home</RouterLink>
                    <RouterLink to="/explore">Explore</RouterLink>
                    <RouterLink to="/users">My Profile</RouterLink>
                    <RouterLink to="/logout">Logout</RouterLink>
                </ul>
            </nav>
        </header>
        
        <section class="container">
            <RouterView />
        </section>
    </main>
</template>


<style>
    .primary-button {
        background-color: #0275d8;
        border: none;
        color: white;
        padding: 10px;
        width: 300px;
        height: 40px;
    }
</style>

<style scoped>

    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
        font-family: sans-serif;
        text-decoration: none;
        list-style: none;
    }

    .header {
        width: 100%;
        box-shadow: 0 4px 20px hsla(207, 24%, 35%, 0.1);
        background-color: #0275d8;
    }

    nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 30px;
    }

    .logo a {
        font-size: 24px;
        font-weight: bold;
        color: #fff;
    }

    .logo a span {
        color: #fff;
    }

    .logo-image {
        width: 25px;
        margin-right: 10px;
    }

    .menu {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .menu a {
        display: block;
        padding: 7px 15px;
        font-size: 17px;
        font-weight: 500;
        transition: 0.2s all ease-in-out;
        color: #fff;
    }

    .menu:hover a {
        opacity: 0.4;
    }

    .menu a:hover {
        opacity: 1;
        color: #fff;
    }

    .menu-icon {
        display: none;
    }

    .container {
        min-height: 90vh;
        padding-top: 5vh;
        background-color: #e1e1cc;

    }

</style>