<template>
<div class="container">
  <div class="q-mt-xl" style="max-width: 350px">
    <h4>Возможные действия</h4>
    <q-file filled v-model="model" class="bg-light-green-14 q-mb-lg rounded-borders" color="red" label-color="white" label="Добавить баннер" label-slot></q-file>
    <q-file filled v-model="model" class="bg-light-green-14 q-mb-lg rounded-borders" color="red" label-color="white" label="Экспорт чеков" label-slot></q-file>
    <q-file filled v-model="model" class="bg-light-green-14 q-mb-lg rounded-borders" color="red" label-color="white" label="Экспорт кэшбэков" label-slot></q-file>
    <q-file filled v-model="model" class="bg-light-green-14 q-mb-lg rounded-borders" color="red" label-color="white" label="Импорт кэшбэков" label-slot></q-file>
  </div>
</div>
</template>

<script>
export default {
  name: "DataComp",
  data(){
    return{
      model:null,
    }
  }
};
</script>

<style scoped>

</style>
