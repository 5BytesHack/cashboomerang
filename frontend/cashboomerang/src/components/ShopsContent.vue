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
    <div class="q-pt-md" v-for="shop in $store.state.popularShops" :key="shop.name">
      <group-card  :title="shop.name"
                   :items="shop.cashback">
      </group-card>
    </div>
  </div>
</template>

<script>
import GroupCard from "components/GroupCard";
export default {
  name: "ShopsContent",
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
