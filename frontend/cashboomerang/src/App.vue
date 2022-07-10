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
  }
})
</script>
