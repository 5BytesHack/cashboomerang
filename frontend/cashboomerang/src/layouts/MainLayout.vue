<template>
  <q-layout>
    <div class="bg-grey-14">
      <div class="container">
        <q-toolbar class="q-pt-sm  row items-start q-px-md  text-white">
          <q-avatar size="3.1rem">
            <img src="../assets/header/logo.svg" @click="backToMainScreen">
          </q-avatar>

          <q-toolbar-title class="xs-hide">CashBoomerang</q-toolbar-title>
          <q-space></q-space>
          <div class="column">
            <q-btn style="margin-bottom: 0.1rem;" class="q-pa-1" flat dense>
              <router-link :to="rout_str"><img style="width:1.4rem" src="../assets/header/userLogo.svg"/></router-link>
            </q-btn>
            <q-badge color="red q-mb-sm">ID: {{userId}}</q-badge>
          </div>
        </q-toolbar>
      </div>
    </div>
    <q-dialog v-model="prompt" persistent>
      <q-card style="min-width: 350px;">
        <q-card-section class="bg-grey-14">
          <div class="text-h6 text-white">Введите Ваш ID</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense autofocus @keyup.enter="prompt = false" color="grey-14"/>
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn label="Войти" style="border-radius: 13px" class="bg-red q-px-lg q-py-xs text-white" />
        </q-card-actions>
      </q-card>
    </q-dialog>
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
      userId:'5745',
      prompt: ref(true)
    }
  },
  computed:{
    rout_str: function() {
      return "profile/" + this.userId.toString();
    }
  },
  methods:{
    backToMainScreen(){
      this.$router.push("/");
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
