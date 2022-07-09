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
  <div class="q-pt-md" v-for="Gr in GroupCards" :key="Gr.title">
    <group-card  :title="Gr.title" :items="Gr.items"
    :link="Gr.link"></group-card>
  </div>

</div>
</template>

<script>
import { ref } from "vue/dist/vue";
import GroupCard from "components/GroupCard";

export default {
  name: "GoodsContent",
  components:{
    GroupCard,
  },
  props:['GroupCards'],
  data(){
    return{

      text: '',//(''),
      readonly: ref(false),
      disable: ref(false)
    }
  }
};
</script>

<style scoped>

</style>
