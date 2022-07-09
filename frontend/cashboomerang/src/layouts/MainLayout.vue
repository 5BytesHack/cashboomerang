<template>
  <q-layout>
    <q-page-container>
      <category-select></category-select>
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue'
import CategorySelect from "components/CategorySelect";
export default defineComponent({
  name: 'MainLayout',

  components: {
    CategorySelect
  },

  data(){
    return{

    }
  }
})
</script>
