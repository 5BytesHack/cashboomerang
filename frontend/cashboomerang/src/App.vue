<template>

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
      //await this.$store.dispatch('recommend/getRecommendations', this.userId);
      await this.$store.dispatch('recommend/getPopularProducts');
    }
  }
})
</script>
