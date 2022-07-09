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
  </div>
</template>

<script>
import { ref } from "vue/dist/vue";

export default {
  name: "ShopsContent",
  data(){
    return{
      text: '',//ref(''),
      readonly: ref(false),
      disable: ref(false)
    }
  }
};
</script>

<style scoped>

</style>
