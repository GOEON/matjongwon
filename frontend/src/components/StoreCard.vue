<template>
  <div>
    <b-card no-body class="overflow-hidden" style="max-width: 540px;" :href="url">
      <b-carousel class="rounded-0"
          controls
          indicators
          :interval="0"
      >
        <b-carousel-slide
          v-for="(item, i) in thumbnails" :key="i"
          :img-src="item"
        >
        </b-carousel-slide>
      </b-carousel>
      <b-card-body :title="name">
        <b-card-sub-title>
          {{ getCategoryName }}
          <b-img :width="20" :height="20" :src="require(`@/assets/images/kakaomap_icon.png`)" v-if="score.kakaomap"></b-img><span>{{ score.kakaomap }}</span>
          <b-img :width="20" :height="20" :src="require(`@/assets/images/navermap_icon.png`)" v-if="score.navermap"></b-img><span>{{ score.navermap }}</span>
        </b-card-sub-title>
        <b-card-text>
          {{ getDescriptions }}
        </b-card-text>
        <a :href="reviews.navermap" class="card-link">네이버 리뷰</a>
        <a :href="reviews.kakaomap" class="card-link">카카오 리뷰</a>
      </b-card-body>
      <b-list-group flush>
        <b-list-group-item>{{ address }}</b-list-group-item>
        <b-list-group-item>{{ menu }}</b-list-group-item>
      </b-list-group>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "StoreCard",
  props: {
    name: {type: String},
    category: {type: Array},
    description: {type: String},
    address: {type: String},
    openingHours: {type: String},
    score: {type: Object},
    menu: {type: String},
    thumbnails: {type: Array},
    url: {type: String},
    reviews: {type: String},
  },
  computed: {
    getCategoryName() {
      return this.category.join(", ");
    },
    getDescriptions() {
      if (this.description) {
        return this.description.substring(1,70) + "...";
      }
      return "";
    }
  },
  data() {
    return {
    };
  },
}
</script>

<style></style>