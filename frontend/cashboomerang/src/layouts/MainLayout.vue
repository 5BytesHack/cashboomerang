<template>
  <q-layout>
    <div class="header-card-wrapper q-pt-md q-px-md">
      <q-carousel
        animated
        v-model="slide"
        class="slider shadow-4 rounded-borders"
        swipeable
        navigation
        control-color="grey"
        style="height: 66vw; max-height: 920px; max-width: 1420px; margin: 0 auto;"
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
import "../css/app.scss";
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
