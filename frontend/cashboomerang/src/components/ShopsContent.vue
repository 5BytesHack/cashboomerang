<template>
  <div>
    <q-input  color="grey"
              v-model="text"
              :readonly="readonly"
              outlined rounded
              :disable="disable"
              label-color="grey"
              label="Поиск..."
              class="font-size">
      <template v-slot:append>
        <q-icon name="search" />
      </template>
    </q-input>
    <div v-if="$store.state.popularShops.length">
      <group-card  :title="'Часто посещаемые магазины'"
                   :items="$store.state.popularShops"
                   :link="''">
      </group-card>
    </div>
  </div>
</template>

<script>
import groupCard from "components/GroupCard";
export default {
  name: "ShopsContent",
  components:{
    groupCard
  },
  data(){
    return{
      text: '',//ref(''),
      readonly: false,
      disable: false
    }
  }
};
</script>

<style scoped>

</style>
