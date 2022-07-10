import api from './api.js';

export default {
  namespaced: true,
  state: () => ({

  }),
  mutations: {

  },
  actions: {
    async getRecommendations(context, userId){
      console.log('userId',userId);
       context.commit('se', await api.recommendations(userId),{root:true});
    },
    async getPopularProducts({rootState}){
      await api.popularproducts();
    }
  },
  getters: {  }
}
