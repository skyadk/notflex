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
    path: '/movielist',
    name: 'MovieList',
    component: () => import('../views/MovieList.vue'),
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/user/Login.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
