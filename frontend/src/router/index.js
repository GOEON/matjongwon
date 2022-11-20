import Vue from 'vue'
import Router from 'vue-router'
import AppHeader from "../layout/AppHeader";
import AppFooter from "../layout/AppFooter";
import MainMap from "../views/MainMap.vue";
import MainList from "../views/MainList.vue";

Vue.use(Router)

export default new Router({
  mode:'history', //해쉬값 제거 방식
  routes: [
    {
      path: "/",
      name: "main",
      redirect: "/map",
      components: {
        header: AppHeader,
        default: MainMap,
        footer: AppFooter
      },
      children: [
        {
          path: '/map',
          name: 'map',
          components: {
            header: AppHeader,
            default: MainMap,
            footer: AppFooter
          },
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
      ]
    },
  ]
})