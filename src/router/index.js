import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue';
import RegisterView from '../views/RegisterView.vue';
import LoginView from '../views/LoginView.vue';
import LogoutView from '../views/LogoutView.vue';
import ExploreView from '../views/ExploreView.vue';
import ProfileView from '../views/ProfileView.vue';
import NewPostView from '../views/NewPostView.vue';

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogoutView
    },
    {
      path: '/explore',
      name: 'explore',
      component: ExploreView
    },
    {
      path: '/users', // Update for id when routes are integrated
      name: 'users',
      component: ProfileView
    },
    {
      path: '/posts/new',
      name: 'posts/new',
      component: NewPostView
    },
  ]
})

export default router;