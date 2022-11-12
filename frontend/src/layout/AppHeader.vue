<template>
  <div>
    <b-navbar toggleable="sm" variant="light">
      <b-navbar-toggle @click="toggleSidebar"></b-navbar-toggle>

      <b-navbar-brand href="/">맛종원</b-navbar-brand>

      <b-nav-form class="w-50">
          <b-form-input placeholder="검색"></b-form-input>
        </b-nav-form>
        
        <b-nav tabs pills>
          <b-nav-item size="sm" :active="tabActiveKey === 1" @click="() => {tabActiveKey = 1}">지도</b-nav-item>
          <b-nav-item size="sm" :active="tabActiveKey === 2" @click="() => {tabActiveKey = 2}">목록</b-nav-item>
        </b-nav>
      <b-navbar-nav>
        <b-collapse is-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
              <b-nav-item href="#">로그인</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar-nav>
      
      <b-sidebar>
        <div class="p-3">
          <h4 id="sidebar-no-header-title">Custom header sidebar</h4>
          <p>
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
            in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
          </p>
          <nav class="mb-3">
            <b-nav vertical>
              <b-nav-item active @click="hide">Active</b-nav-item>
              <b-nav-item href="#link-1" @click="hide">Link</b-nav-item>
              <b-nav-item href="#link-2" @click="hide">Another Link</b-nav-item>
            </b-nav>
          </nav>
          <b-button variant="primary" block @click="hide">Close Sidebar</b-button>
        </div>
      </b-sidebar>
    </b-navbar>
  </div>
</template>
<script>
export default {
  data() {
    return {
        tabActiveKey: 1,
        sidebarActive: false,
    }
  },
  methods: {
    toggleSidebar() {
      this.sidebarActive = !this.sidebarActive;
    }
  }
};
</script>
<style>
@media only screen and (max-width: 576px) {
  .navbar-brand {
    display: none !important;
  }
}

</style>
