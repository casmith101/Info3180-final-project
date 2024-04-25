<template>
    <seciton class="profile-container">
        <div class="profile-info-container">
            <div class="image-container">
                <img src="../assets/user.png" alt="Post" class="image"/>
            </div>

            <div class="profile-info">
                <h3>Rosa Diaz</h3>

                <div>
                    <p>Kingston, Jamaica</p>
                    <p>Member since January 2018</p>
                </div>

                <p>This is my short biography so you can learn more about me</p>
            </div>

            <div>
                <div>
                    <div>
                        <h3>6</h3>
                        <p>Posts</p>
                    </div>

                    <div>
                        <h3>10</h3>
                        <p>Followers</p>
                    </div>
                </div>

                <button class="primary-button">New Post</button>
            </div>
        </div>
    </seciton>
</template>

<style scoped>

    .profile-container {
        width: 100%;
    }

    .profile-info-container {
        display: flex;
        container: 100%;
        background-color: white;
        border-radius: 5px;
        padding: 0.5rem;
    }

    .image {
        width: 100px;
    }

</style>