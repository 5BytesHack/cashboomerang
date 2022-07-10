<template>
  <q-btn @click="api">API</q-btn>
  <div class="bg-grey-14">
    <div class="container">
      <q-toolbar class="q-pt-sm  row items-start q-px-md  text-white">
        <q-avatar size="3.1rem">
          <img src="./assets/header/logo.svg" @click="backToMainScreen">
        </q-avatar>

        <q-toolbar-title class="xs-hide">CashBoomerang</q-toolbar-title>
        <q-space></q-space>
        <div class="column">
          <q-btn style="margin-bottom: 0.1rem;" class="q-pa-1" flat dense>
            <router-link :to="rout_str"><img style="width:1.4rem" src="./assets/header/userLogo.svg"/></router-link>
          </q-btn>
          <q-badge color="red q-mb-sm">ID: {{userId}}</q-badge>
        </div>
      </q-toolbar>
    </div>
  </div>
  <router-view />
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'App',
  data(){
    return{
      userId:'1'
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
    },
    async api(){
      await this.$store.dispatch('recommend/getRecommendations', this.userId);
    }
  }
})
</script>
