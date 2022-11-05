import {createWebHistory, createRouter} from "vue-router";
import AppHeader from "./layout/AppHeader";
import AppFooter from "./layout/AppFooter";
import Main from "./views/Main.vue";

const routes = createRouter({
  linkExactActiveClass: "active",
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "main",
      components: {
        header: AppHeader,
        default: Main,
        footer: AppFooter
      }
    }
  ],
  scrollBehavior: to => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  }
});

export default routes;