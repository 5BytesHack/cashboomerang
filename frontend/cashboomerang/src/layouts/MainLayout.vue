<template>
  <q-layout>
    <div>
      <q-toolbar class="q-pt-sm  row items-start q-px-md bg-grey-14 text-white">
        <q-avatar size="3.1rem">
          <img src="../assets/header/logo.svg">
        </q-avatar>

        <q-toolbar-title class="xs-hide">CashBoomerang</q-toolbar-title>
        <q-space></q-space>
        <div class="column">
          <q-btn style="margin-bottom: 0.1rem;" class="q-pa-1" flat dense>
            <img style="width:1.4rem" src="../assets/header/userLogo.svg"/>
          </q-btn>
          <q-badge color="red q-mb-sm">ID: {{userId}}</q-badge>
        </div>
      </q-toolbar>
    </div>

    <div class="header-card-wrapper q-pt-md q-px-md">
      <q-carousel
        animated
        v-model="slide"
        class="slider shadow-4 rounded-borders"
        swipeable
        navigation
        control-color="grey"
        offset="[359,265]"
      >
        <q-carousel-slide :name="1"  img-src="../assets/header/cards/1.svg">
<!--          <img src="../assets/header/cards/1.svg" />-->
        </q-carousel-slide>
        <q-carousel-slide :name="2"  img-src="../assets/header/cards/2.svg"></q-carousel-slide>
      </q-carousel>
    </div>
    <div class="">
      <category-select></category-select>
    </div>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import CategorySelect from "components/CategorySelect";
export default defineComponent({
  name: 'MainLayout',
  components: {
    CategorySelect

  },

  data(){
    return{
      slide: ref(1),
      userId:'5745'
    }
  }
})
</script>
<style scoped>
.header-card-wrapper{
  position: relative;
}
.slider{
  border-radius: 20px;
}
.q-carousel__slide{
  padding: 0;
}
</style>
