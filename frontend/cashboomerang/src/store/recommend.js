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
       context.commit('setRecommended', await api.recommendations(userId),{root:true});
    },
    async getPopularProducts(context){
      context.commit('setPopular', await api.popularproducts(),{root:true});
    },
    async getPopularShops(context, userId){
      context.commit('setPopularShops',await api.popularshops(userId),{root:true});
    }
  },
  getters: {  }
}
