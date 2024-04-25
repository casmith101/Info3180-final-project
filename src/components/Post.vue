<template>
    <div class="post">
        <div class="header">
            <img src="../assets/user.png" alt="Post" class="small-image"/>
            <span>user</span>
        </div>

        <img src="../assets/post.jpg" alt="Post" class="image"/>
        <p class="text">Sometimes its just about the mountains</p>
        
        <div class="footer">
            <div class="like-container">
                <img src="../assets/heart.png" alt="Like" class="small-image like-image"/>
                <span class="bold">10 likes</span>
            </div>
            
            <div>
                <p class="bold">24 Apr 2018</p>
            </div>
        </div>
    </div>
</template>

<style scoped>

    .post {
        min-height: 500px;
        width: 700px;
        background-color: white;
        border-radius: 2px;
        border: 1px solid silver;
    }

    .header {
        padding: 10px;
        display: flex;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .image {
        width: 100%;
        height: 300px;
    }

    .small-image {
        width: 20px;
    }

    .text {
        padding: 10px;
        margin-bottom: 1rem;
    }

    .like-image {
        margin-right: 5px;
    }

    .bold {
        font-weight: 550;
    }


    .footer {
        display: flex;
        justify-content: space-between;
        padding: 0px 10px;
    }
</style>