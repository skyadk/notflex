import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/main',
    name: 'Main',
    component: () => import('../views/Main.vue'),
  },
  {
    path: '/mainvuex',
    name: 'Mainvuex',
    component: () => import('../views/MainVuex.vue'),
  },
  {
    path: '/detail/:id',
    name: 'Detail',
    component: () => import('../views/MovieDetail.vue'),
  },
  {
    path: '/movielist',
    name: 'MovieList',
    component: () => import('../views/MovieList.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/user/Login.vue'),
  },
  {
    path: '/signup',
    name: 'Signup',
    component: () => import('@/views/user/Signup.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
