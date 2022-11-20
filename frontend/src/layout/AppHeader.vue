<template>
  <div>
    <b-navbar toggleable="sm" variant="light">
      <b-navbar-toggle target="sidebar-1" v-b-toggle.sidebar-1></b-navbar-toggle>

      <b-navbar-brand href="/">맛종원</b-navbar-brand>

      <b-navbar-nav class="ml-auto w-50">
        <b-nav-form class="mw-100">
          <b-form-input class="mw-100" placeholder="검색"></b-form-input>
        </b-nav-form>
      </b-navbar-nav>
      
      <b-nav pills class="ml-auto">
        <b-nav-item size="sm" :active="gnb === 'map'"  @click="clickGnb('map')" href="/">지도</b-nav-item>
        <b-nav-item size="sm" :active="gnb === 'list'" @click="clickGnb('list')" href="/list">목록</b-nav-item>
      </b-nav>

      <!--b-navbar-nav class="ml-auto">
        <b-nav-item href="#">로그인</b-nav-item>
      </b-navbar-nav-->
      
      <b-sidebar id="sidebar-1" title="Sidebar" shadow>
        <div class="px-3 py-2">
          <p>
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
            in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
          </p>
          <b-img src="https://picsum.photos/500/500/?image=54" fluid thumbnail></b-img>
        </div>
      </b-sidebar>
    </b-navbar>
  </div>
</template>
<script>

import {mapMutations, mapState} from 'vuex';

export default {
  computed: {
    ...mapState(['gnb']),
  },

  methods: {
    clickGnb(gnb) {
      this.setGnb(gnb);
    }
  },
};
</script>
<style>
@media only screen and (max-width: 576px) {
  .navbar-brand {
    display: none !important;
  }
}
</style>
