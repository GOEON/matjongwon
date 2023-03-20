<template>
  <h1>
    {{ authrization_code }}
  </h1>
</template>

<script>
export default {
  created() {
    if (this.$route.query.code) {
      this.setKakaoToken();
    }
  },

  mounted() {
    console.log("mounted");
  },

  data() {
    return {
      authrization_code: "aa"
      // mounted(){
      //   const naver_id_login = new window.naver_id_login("H7fiZLOYxRZdAdDmsOCv", "http://localhost:8080/login/naver");
      //   const state = naver_id_login.getUniqState();
      //   naver_id_login.setButton("white", 2,40); // 버튼 설정
      //   naver_id_login.setState(state);
      //   // naver_id_login.setPopup(); // popup 설정을 위한 코드
      //   naver_id_login.init_naver_id_login();
      // }
    };
  },
  methods: {
    async setKakaoToken() {
      console.log("카카오 인증 코드", this.$route.query.code);
      const { data } = await getKakaoToken(this.$route.query.code);
      if (data.error) {
        alert("카카오톡 로그인 오류입니다.");
        this.$router.go();
        return;
      }
      window.Kakao.Auth.setAccessToken(data.access_token);
      this.$cookies.set("access-token", data.access_token, "1d");
      this.$cookies.set("refresh-token", data.refresh_token, "1d");
      await this.setUserInfo();
      this.$router.push({ name: "home" });
    },
    async setUserInfo() {
      const res = await getKakaoUserInfo();
      console.log(res);
      const userInfo = {
        name: res.kakao_account.profile.nickname,
        platform: "kakao"
      };
      console.log(userInfo);
      // this.$store.commit("setUser", userInfo);
    }
  }
};
</script>

<!-- https://github.com/DinnerKang/study_vue/blob/master/todo-list/front/src/services/login.js -->
