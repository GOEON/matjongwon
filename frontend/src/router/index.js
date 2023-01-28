import Vue from 'vue'
import Router from 'vue-router'
import AppHeader from "../layout/AppHeader";
import AppFooter from "../layout/AppFooter";
import MainMap from "../views/MainMap.vue";
import MainList from "../views/MainList.vue";
import KakaoLogin from "../views/KakaoLogin.vue";
import NaverLogin from "../views/NaverLogin.vue";

Vue.use(Router)

export default new Router({
  mode: 'history', //해쉬값 제거 방식
  routes: [
    {
      path: "/",
      name: "main",
      components: {
        header: AppHeader,
        default: MainMap,
        footer: AppFooter
      }
    },
    {
      path: '/list',
      name: 'list',
      components: {
        header: AppHeader,
        default: MainList,
        footer: AppFooter
      },
    },
    {
      path: '/login',
      name: 'login',
      components: {
        header: AppHeader,
        default: KakaoLogin,
        footer: AppFooter
      }
    },
    {
      path: '/naver_login',
      name: 'naver_login',
      components: {
        header: AppHeader,
        default: NaverLogin,
        footer: AppFooter
      }
    }
  ]
})
