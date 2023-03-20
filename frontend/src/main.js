// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import BootstrapVue from "bootstrap-vue";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.config.productionTip = false;
window.Kakao.init("f0ad268d23009b5d12e685563fba56f8");
Vue.use(BootstrapVue);

/* eslint-disable no-new */
new Vue({
  render: h => h(App),
  store,
  router
}).$mount("#app");
