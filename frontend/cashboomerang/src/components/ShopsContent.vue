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
  </div>
</template>

<script>

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
