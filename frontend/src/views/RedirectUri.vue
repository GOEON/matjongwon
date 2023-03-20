<template>
  <h1>
    {{ authrization_code }}
  </h1>
</template>

<script>
export default {
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
  }
};
</script>
