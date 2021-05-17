import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import store from '@/store/index';

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
    components: { default: () => import('../views/Main.vue'), header: () => import('../views/layout/MainNavbar.vue') },
    meta: { auth: false },
  },
  {
    path: '/detail/:id',
    name: 'Detail',
    components: { default: () => import('../views/MovieDetail.vue'), header: () => import('../views/layout/MainNavbar.vue') },
    meta: { auth: false },
  },
  {
    path: '/search',
    name: 'Search',
    components: { default: () => import('../views/Search.vue'), header: () => import('../views/layout/MainNavbar.vue') },
    meta: { auth: false },
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
  {
    path: '/profile',
    name: 'Profile',
    components: { default: () => import('@/views/Profile.vue'), header: () => import('../views/layout/MainNavbar.vue') },
  },
  {
    path: '/recommended',
    name: 'Recommended',
    components: { default: () => import('@/views/Recommended.vue'), header: () => import('../views/layout/MainNavbar.vue') },
  },
  {
    path: '*',
    redirect: '/404',
  },
  {
    path: '/404',
    name: '404',
    component: () => import('@/views/404.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.meta.auth && !store.state.email) {
    Vue.swal({
      icon: 'error',
      title: '로그인후 사용가능한 서비스입니다.',
      showConfirmButton: false,
      timer: 1500,
    });
    next('/login');
    return;
  }
  next();
});
export default router;
