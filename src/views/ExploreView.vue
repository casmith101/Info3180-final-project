<script setup>
    import Post from '../components/Post.vue';
</script>

<template>
    <section class="explore-container">
        <div class="post-container">
            <Post />
            <Post />
            <Post />
        </div>

        <div class="button-container">
            <button class="primary-button">New Post</button>
        </div>
    </section>
</template>


<style scoped>

    .explore-container {
        display: flex;
        justify-content: center;
        width: 90vw;
        padding-bottom: 2rem;
        margin-left: 5vw;
    }

    .post-container {
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }

    .button-container {
        display: flex;
        width: 100%;
        justify-content: center;
    }
</style>