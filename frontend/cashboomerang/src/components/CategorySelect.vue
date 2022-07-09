<template>
  <div class="category-selector q-pa-md">
    <div class="q-gutter-y-md">
      <q-tabs
        class="no-shadow border-bottom"
        v-model="tab"
        inline-label
        indicator-color="red"
      >
        <q-tab name="goods" icon="" label="Товары" @click="CurrentComponent='GoodsContent'" class="text-h4"/>
        <q-tab name="shop" icon="" label="Магазины" @click="CurrentComponent='ShopsContent'"/>
      </q-tabs>
     <keep-alive> <component :is="CurrentComponent" :GroupCards="data"></component></keep-alive>
    </div>
  </div>

</template>

<script>
import goods from '../assets/exampleData/goods.js'
import {ref} from 'vue'
import GoodsContent from "components/GoodsContent";
import ShopsContent from "components/ShopsContent";
export default {
  name: "CategorySelect",
  components:{
    GoodsContent,
    ShopsContent
  },
  data(){
    return{
      data: goods.data,
      tab: ref('goods'),
      CurrentComponent: 'GoodsContent',
    }
  },
};
</script>

<style scoped>
  .border-bottom{
    border-bottom: 1px solid gray;
  }
  .font-size{
    font-size: 1.1rem;
  }
</style>
