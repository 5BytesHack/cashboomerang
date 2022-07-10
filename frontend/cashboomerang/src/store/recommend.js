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
      rootState.productsInfo = await api.recommendations(userId);
    }
  },
  getters: {  }
}
