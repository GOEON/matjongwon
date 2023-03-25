<template>
  <div>
    <b-navbar toggleable="sm" variant="light">
      <b-navbar-toggle
        target="sidebar-1"
        v-b-toggle.sidebar-1
      ></b-navbar-toggle>

      <b-navbar-brand href="/">맛종원</b-navbar-brand>

      <b-navbar-nav class="ml-auto w-50">
        <b-nav-form class="mw-100">
          <b-form-input class="mw-100" placeholder="검색"></b-form-input>
        </b-nav-form>
      </b-navbar-nav>

      <b-nav pills class="ml-auto">
        <b-nav-item
          size="sm"
          :active="gnb === 'map'"
          @click="clickGnb('map')"
          href="/"
          >지도</b-nav-item
        >
        <b-nav-item
          size="sm"
          :active="gnb === 'list'"
          @click="clickGnb('list')"
          href="/list"
          >목록</b-nav-item
        >
        <b-nav-item size="sm" v-b-toggle.sidebar-right>
          로그인
          <b-sidebar
            id="sidebar-right"
            title="로그인"
            width="350px"
            right
            shadow
          >
            <div class="px-3 py-2" style="text-align:center">
              <h4>로그인을 하면 가고싶은 식당을 저장할 수 있어요</h4>
              <br />
              <div>
                <img
                  src="../assets/images/kakao_login_button.png"
                  alt=""
                  width="320px"
                  height="80px"
                  @click="kakaoLogin()"
                />
              </div>
              <br />
              <div>
                <img
                  src="../assets/images/naver_login_button.png"
                  alt=""
                  width="320px"
                  height="80px"
                  @click="naverLogin()"
                />
              </div>
            </div>
          </b-sidebar>
        </b-nav-item>
        <b-nav-item size="sm" v-b-toggle.sidebar-right>
          <!-- <img
            src="https://cdn-icons-png.flaticon.com/512/6522/6522516.png"
            alt=""
            width="18px"
            height="auto"
          /> -->
          <!-- <b-sidebar
            id="sidebar-right"
            title="프로필"
            width="350px"
            right
            shadow
          >
            <button>로그아웃</button>
          </b-sidebar> -->
        </b-nav-item>
      </b-nav>
      <b-sidebar id="sidebar-1" shadow>
        <div class="px-3 py-2"></div>
      </b-sidebar>
    </b-navbar>
  </div>
</template>
<script>
import { mapMutations, mapState } from "vuex";
import axios from "axios";

export default {
  

  created()  {
    console.log('AppHeader is created!!')
  },

  data() {
    return {
      user_info : '',
    }
  },
  computed: {
    ...mapState(["gnb"])
  },
  methods: {
    ...mapMutations(["setGnb"]),

    clickGnb(gnb) {
      this.setGnb(gnb);
    },

    kakaoLogin() {
      const params = {
        redirectUri: "http://localhost:8000/oauth/kakao/callback"
      };
      window.Kakao.Auth.authorize(params);
    },

    naverLogin() {
      // const naver_id_login = new window.naver_id_login(
      //   "H7fiZLOYxRZdAdDmsOCv",
      //   "http://localhost:5000/oauth/callbacks"
      // );
      console.log("네이버 로그인")
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
