<template>
  <div>
    <!-- <a id="custom-login-btn" @click="kakaoLogin()">
      <img
        src="//k.kakaocdn.net/14/dn/btqCn0WEmI3/nijroPfbpCa4at5EIsjyf0/o.jpg"
        width="222"
      />
    </a> -->
  </div>
</template>

<script>
export default {
  methods: {
    kakaoLogin() {
      console.log(window.Kakao);
      window.Kakao.Auth.login({
        scope: "profile_nickname, account_email, gender, age_range, birthday",
        success: this.getKakaoAccount
      });
    },
    getKakaoAccount() {
      window.Kakao.API.request({
        url: "/v2/user/me",
        success: res => {
          const kakao_account = res.kakao_account;
          const nickname = kakao_account.nickname;
          const email = kakao_account.email;
          const gender = kakao_account.gender;
          const birthday = kakao_account.birthday;
          console.log("nickname", nickname);
          console.log("email", email);
          console.log("gender", gender);
          console.log("birthday", birthday);
        },
        fail: error => {
          console.log(error);
        }
      });
    }
  }
};
</script>
