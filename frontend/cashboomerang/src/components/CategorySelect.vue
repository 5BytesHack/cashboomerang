<template>
  <div class="q-pa-md">
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
      data:[
        {
        title: "Часто покупаемые",
        link: "1",
        items:[
          {
            name: "Гречка",
            src2: "../assets/ItemDefaultIcon.png",
            cash: '1,1',
          },
          {
            name: "Овсянка",
            src2: "../assets/ItemDefaultIcon.png",
            cash: '1,2',
          },
          {
            name: "Манка",
            src2: "../assets/ItemDefaultIcon.png",
            cash: '1,3',
          }
        ]
        },
        {
          title: "Редко покупаемые",
          link: "2",
          items:[
            {
              name: "Drive желтый",
              src2: "../assets/ItemDefaultIcon.png",
              cash: '2,1',
            },
            {
              name: "Drive синий",
              src2: "../assets/ItemDefaultIcon.png",
              cash: '2,1',
            },
            {
              name: "Гречка",
              src2: "../assets/ItemDefaultIcon.png",
              cash: '3,1',
            }
          ]
        }],
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
