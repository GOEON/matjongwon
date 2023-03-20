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
        <b-nav-item size="sm" v-b-toggle.sidebar-right v-if="!kakao_account">
          로그인
          <b-sidebar
            id="sidebar-right"
            title="로그인"
            width="350px"
            right
            shadow
          >
            <div class="px-3 py-2" style="text-align:center">
              <h4>
                로그인을 하면 가고싶은 식당을 저장할 수 있어요
              </h4>
              <br />
              <div>
                <img
                  src="https://asp.pointpark.com/PlusPointMember/resources/images/mobileHomePage/btn_kakao.png"
                  alt=""
                  width="320px"
                  @click="kakaoLogin()"
                />
              </div>
            </div>
          </b-sidebar>
        </b-nav-item>
        <b-nav-item size="sm" v-b-toggle.sidebar-right v-if="kakao_account">
          <img
            src="https://cdn-icons-png.flaticon.com/512/6522/6522516.png"
            alt=""
            width="18px"
            height="auto"
          />
          <b-sidebar
            id="sidebar-right"
            title="프로필"
            width="350px"
            right
            shadow
          >
            <div class="px-3 py-2" style="text-align:left">
              <!-- 닉네임 : {{ kakao_account.nickname }} </br> -->
              이메일 : {{ kakao_account.email }} </br>
              성별 : {{ kakao_account.gender }} </br>
              연령대 : {{ kakao_account.age_range }} </br>
              생일 : {{ kakao_account.birthday }} </br>
            </div>
            <button @click="kakaoLogout()">로그아웃</button>
          </b-sidebar>
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

export default {
  computed: {
    ...mapState(["gnb"])
  },
  data() {
    return {
      // accessToken: window.Kakao.Auth.getAccessToken()
      kakao_account: false
    };
  },

  methods: {
    ...mapMutations(["setGnb", "setLoginToken"]),

    clickGnb(gnb) {
      this.setGnb(gnb);
    },
    clickToken(token) {
      this.setLoginToken(token);
    },
    kakaoLogin() {
      window.Kakao.Auth.login({
        scope: "profile_nickname, account_email, gender, age_range, birthday",
        success: this.getKakaoAccount
      });
      alert("로그인 성공");
    },
    getKakaoAccount() {
      window.Kakao.API.request({
        url: "/v2/user/me",
        success: res => {
          this.kakao_account = res.kakao_account;
        },
        fail: error => {
          console.log(error);
        }
      });
    },
    kakaoLogout() {
      window.Kakao.Auth.logout(response => {
        console.log(response);
      });
      alert("로그아웃 되었습니다.")
      this.kakao_account = false
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
body {
  margin: 0;
}
div {
  box-sizing: border-box;
}
.black-bg {
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  padding: 20px;
}
.white-bg {
  width: 100%;
  background: white;
  border-radius: 8px;
  padding: 20px;
}
</style>
