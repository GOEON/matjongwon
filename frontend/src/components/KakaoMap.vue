<template>
  <div id="kakaomap"></div>
</template>

<script>
// https://goodteacher.tistory.com/432
export default {
  name: "KakaoMap",
  data() {
    return {
      kakaomap: null
    };
  },
  mounted() {
    window.kakao && window.kakao.maps ? this.initMap() : this.addKakaoMapSdk();
  },
  methods: {
    initMap() {
      const container = document.getElementById("kakaomap");
      const options = {
        center: new kakao.maps.LatLng(37.498095, 127.02761, 16),
        level: 5
      };
      this.kakaomap = new kakao.maps.Map(container, options);
      console.log("map created");
    },
    addKakaoMapSdk() {
      const script = document.createElement("script");
      script.src =
        "//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=a82e397860bdddf2149271fcc898e75a";
      script.onload = () => kakao.maps.load(this.initMap);
      document.head.appendChild(script);
    }
  }
};
</script>
<style>
#kakaomap {
  width: 100%;
  height: 1000px;
}
</style>
