<template>
  <q-layout>
    <div>
      <q-toolbar class="q-pt-sm q-pb-xl row items-start q-px-md bg-grey-14 text-white">
        <q-avatar size="4.5rem">
          <img src="../assets/header/logo.svg">
        </q-avatar>

        <q-toolbar-title class="xs-hide">CashBoomerang</q-toolbar-title>
        <q-space></q-space>
        <div class="column">
          <q-btn style="margin-bottom: 0.1rem;" class="q-pa-1" flat dense>
            <img style="width:2.5rem" src="../assets/header/userLogo.svg"/>
          </q-btn>
          <q-badge color="red">ID: {{userId}}</q-badge>
        </div>
      </q-toolbar>

      <category-select></category-select>
    </div>
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
      userId:'5745'
    }
  }
})
</script>
