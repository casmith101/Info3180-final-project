<script setup>
    import ProfileInfo from '../components/ProfileInfo.vue';

</script>

<template>
    <seciton>
        <ProfileInfo />

        <div class="gallery">
            <img src="../assets/post.jpg" alt="Post" class="image"/>
            <img src="../assets/post.jpg" alt="Post" class="image"/>
            <img src="../assets/post.jpg" alt="Post" class="image"/>
        </div>
    </seciton>
</template>

<style scoped>
    .gallery {
        display: grid;
        margin-top: 1rem;
        margin-left: 1rem;
        grid-template-columns: 30% 30% 30%;
        grid-gap: 2rem;
    }

    .image {
        width: 30vw;
    }

</style>