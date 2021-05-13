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
  // {
  //   path: '/mainvuex',
  //   name: 'Mainvuex',
  //   component: () => import('../views/MainVuex.vue'),
  // },
  {
    path: '/detail/:id',
    name: 'Detail',
    component: () => import('../views/MovieDetail.vue'),
    meta: { auth: false },
  },
  {
    path: '/movielist',
    name: 'MovieList',
    component: () => import('../views/MovieList.vue'),
    meta: { auth: false },
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('../views/Search.vue'),
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
