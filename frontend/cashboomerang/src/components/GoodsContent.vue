<template>
<div>
  <q-input  color="grey"
            v-model="text"
            :readonly="readonly"
            outlined rounded :disable="disable"
            label-color="grey" label="Поиск..."
            class="font-size">
    <template v-slot:append>
      <q-icon name="search" />
    </template>
  </q-input>
  <div class="q-pt-md">
    <group-card
      v-if="$store.state.productsRecommend.length"
      :title="'Рекомендуемое'"
      :items="$store.state.productsRecommend"
      :link="''">
    </group-card>
    <group-card
      v-if="$store.state.productsPopular.length"
      :title="'Популярное'"
      :items="$store.state.productsPopular"
      :link="''">
    </group-card>
  </div>

</div>
</template>

<script>
import GroupCard from "components/GroupCard";

export default {
  name: "GoodsContent",
  components:{
    GroupCard,
  },
  props:{
    GroupCards:Array
  },
  data(){
    return{
      text: '',//(''),
      readonly: false,
      disable: false
    }
  }
};
</script>

<style scoped>

</style>
