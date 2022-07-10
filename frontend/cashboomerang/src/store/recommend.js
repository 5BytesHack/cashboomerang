import api from './api.js';

export default {
  namespaced: true,
  state: () => ({

  }),
  mutations: {

  },
  actions: {
    async getRecommendations({rootState}, userId){
      console.log('userId',userId);
      await api.recommendations(userId);
    },
    async getPopularProducts({rootState}){
      await api.popularproducts();
    }
  },
  getters: {  }
}
