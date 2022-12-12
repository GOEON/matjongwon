<template>
  <div>
    <b-card no-body class="overflow-hidden" style="max-width: 540px;" :href="url">
      <b-row no-gutters>
        <b-col md="6">
          <b-card-img src="https://picsum.photos/400/400/?image=20" alt="Image" class="rounded-0"></b-card-img>
        </b-col>
        <b-col md="6">
          <b-card-body :title="name" :sub-title="getCategoryName">
            <b-card-text>
              단숨에 양재동 주민들의 마음을 사로잡은 파티시에 부부의 빵집
            </b-card-text>
          </b-card-body>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
export default {
  name: "StoreCard",
  props: {
    name: {type: String},
    category: {type: Array},
    address: {type: String},
    openingHours: {type: String},
    score: {type: Object},
    menu: {type: Object},
    url: {type: String},
    reviews: {type: String},
  },
  computed: {
    getCategoryName() {
      return this.category.join(", ");
    }
  },
  data() {
    return {
    };
  },
}
</script>

<style></style>