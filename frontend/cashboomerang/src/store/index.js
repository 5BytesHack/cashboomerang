import { store } from 'quasar/wrappers'
import { createStore } from 'vuex'
//import productsInfo from "assets/exampleData/productsInfo";
import auth from "src/store/auth";
import recommend from "src/store/recommend";
// import example from './module-example'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default store(function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      // example
      auth,
      recommend
    },
    state:{
      userId:'',
      userEmail:'',
      productsRecommend: [],
      productsPopular: [],
      popularShops:[],
      popupName:'',
      popupIsOpen:false,
      popupCashbacks:[]
    },
    mutations:{
      setPopupName(state, name){
        //state.popupCashbacks = state.productsPopular.products.filter( (x) => x.name == name);
        //state.popupCashbacks = state.productsPopular.products.filter( (x) => x.name == name);
        state.popupName = name;
      },
      setPopupIsOpen(state, value){
        state.popupIsOpen = value;
       },
      setPopupCashbacks(state, value){
        state.popupCashbacks = value;
      },
      setUserId(state, userId){
        state.userId = userId;
      },
      setPopular(state, value){
        state.productsPopular = value;
      },
      setPopularShops(state, value){
        state.popularShops = value;
      },
      setRecommended(state, value){
        state.productsRecommend = value;
      }
    },
    actions:{
      getCashbacksForProduct(context){
        //context.state.popupCashbacks = [1, 2, 3]//context.state.productsInfo.products.filter( (x) => x.name == name);
      },
      setProductsRecommended(context, name){
        const product = context.state.productsRecommend.find( (x) => x.name == name);
        context.commit('setPopupCashbacks', product.shops)
      }
    },
    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    strict: process.env.DEBUGGING
  })

  return Store
})
