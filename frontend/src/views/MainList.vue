<!-- <template>
  <b-card-group v-for:="(store, idx) in stores">
    < <StoreCard
              :name="store.name"
              :category="store.category"
              :address="store.address"
              :openingHours="store.openingHours"
              :score="store.score"
              :menu="store.menu"
              :url="store.url"
              :reviews="store.reviews"
    >
    </StoreCard>>
  </b-card-group>
</template>

<script>
import StoreCard from "../components/StoreCard";

export default {
  components: {
    StoreCard,
  },

  computed: {
    stores() {
      return [
        { 
          "name" : "스케줄 청담", 
          "category" : ["양식"], 
          "address" : "서울 강남구 선릉로152길 37 1층", 
          "opening_hours" : "매일 11:00~01:00", 
          "score" : {
            "kakao_map":"3.8", 
            "tripadvisor": "4.3", 
            "google_map" : "3.9"
          },
          "menu" : {'Americano': '4,000', 'Cafe Latte': '5,000'}, 
          "url" : "https://naver.me/GfaMZAvk", 
          "reviews" : "https://pcmap.place.naver.com/restaurant/1793289940/review?entry=bmp&from=map&fromPanelNum=1&ts=1666535787792" 
        },
        { 
          "name" : "중앙해장", 
          "category" : ["해장국", "국밥"], 
          "address" : "서울 강남구 영동대로 86번길 17 육인빌딩 1층", 
          "opening_hours" : "매일 11:00~22:00", 
          "score" : {
            "kakao_map": "3.8",
            "tripadvisor": "4.4", 
            "google_map" : "3.8"
           },
           "menu" : {'한우양선지 해장국': '12,000', '한우내장탕': '15,000', '한우1++양지곰탕': '14,000', '한우우족탕': '21,000', '한우1++양지수육 (중)': '42,000', '곱창전골 (중)': '65,000'}, 
           "url" : "https://naver.me/5Rct4XVA", 
           "reviews" : "https://pcmap.place.naver.com/restaurant/1493771409/review?entry=bmp&from=map&fromPanelNum=1&ts=1666535835165" }
      ];
    },
  }
};
</script> -->
