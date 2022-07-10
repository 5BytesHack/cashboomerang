<template>
  <div class="category-selector q-pt-sm q-px-md">
    <div class="q-gutter-y-md">
      <q-tabs
        class="no-shadow border-bottom tabs"
        v-model="tab"
        inline-label
        indicator-color="red"
      >
        <q-tab name="goods" icon="" label="Товары" @click="CurrentComponent='GoodsContent'" class="text-h4"/>
        <q-tab name="shop" icon="" label="Магазины" @click="CurrentComponent='ShopsContent'"/>
      </q-tabs>
     <keep-alive> <component :is="CurrentComponent" :GroupCards="data"></component></keep-alive>
    </div>
    <q-dialog full-width v-model="popupIsOpen" :position="position">
      <div style="border-radius: 20px 20px 0 0;overflow-y: hidden">
        <q-card class="">
          <q-card-section style="overflow: hidden" class="row items-center q-pa-none justify-end">
            <q-btn icon="close" flat round dense v-close-popup />
          </q-card-section>
            <q-card-section class="q-pb-lg-sm">
              <h2 class="text-center q-my-none">{{$store.state.popupName}}</h2>
              <div style="overflow-y: scroll;max-height:600px" v-if="popupIsOpen" class="q-pb-xl">
                <popup-item v-for="item in $store.state.popupCashbacks"
                            :key="item.name"
                            :name="item.name"
                            :cash="item.cashback">
                </popup-item>
              </div>
            </q-card-section>
        </q-card>
      </div>
    </q-dialog>
  </div>

</template>

<script>
import {ref} from 'vue'
import goods from '../assets/exampleData/goods.js'
import GoodsContent from "components/GoodsContent";
import ShopsContent from "components/ShopsContent";
import PopupItem from "components/PopupItem";
export default {
  name: "CategorySelect",
  components:{
    GoodsContent,
    ShopsContent,
    PopupItem
  },

  data(){
    return{
      position: 'bottom',
      data: goods.data,
      tab: ref('goods'),
      CurrentComponent: 'GoodsContent',
    }
  },
  methods:{
    open(position){
      this.popupIsOpen = true;
      this.position = position;
    }
  },
  computed:{
    popupIsOpen:{
      get(){
        return this.$store.state.popupIsOpen;
      },
      set(value){
        this.$store.commit('setPopupIsOpen', value);
      }
    },
  }
};
</script>

<style scoped>
  .border-bottom{
    border-bottom: 1px solid gray;
  }
  .tabs{
    max-width: 600px;
    margin-left:  auto;
    margin-right: auto;
  }
  .category-selector{

  }
</style>
