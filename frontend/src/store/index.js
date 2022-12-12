import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  // 글로벌 영역 상태값.
  state: {
     gnb: '', // 선택중인 GNB
  },

  mutations: {
    /**
     * GNB를 선택하는 메소드
     *
     * @param state 저장소
     * @param id 선택된 template type
     */
    setGnb(state, id) {
      state.gnb = id;
    },
  }
});