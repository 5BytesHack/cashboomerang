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
     <keep-alive> <component @cardClicked="showPopup" :is="CurrentComponent" :GroupCards="data"></component></keep-alive>
    </div>
    <q-btn label="Bottom" icon="keyboard_arrow_down" color="primary" @click="open('bottom')" />
    <q-dialog full-width v-model="dialog" :position="position">
      <q-card class="">
        <q-card-section class="row items-center q-pa-none justify-end">
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section>
          <!--        <q-img src="../assets/header/logo.svg"></q-img>-->
          <div v-if="">
            <popup-item :name="'Маргарин'" :cash="'7,3'"></popup-item>
          </div>
        </q-card-section>
      </q-card>
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
      dialog: false,
      position: 'top',
      data: goods.data,
      tab: ref('goods'),
      CurrentComponent: 'GoodsContent',
    }
  },
  methods:{
    showPopup(name){
      const cachbacks = this.$store.dispatch('getCashbacksForProduct', name);
    },
    open(position){
      this.position = position;
      this.dialog = true;
    }
  },
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
