<template>

<div class="relative-position item-container q-pa-sm">
    <img :src="iconSrc" alt=""/>
    <q-badge class="cashback rounded-borders q-py-sm q-px-sm text-white">{{cash}}</q-badge>
    <div class="text-center">
      <p><strong>{{item.name}}</strong></p>
    </div>
</div>


</template>

<script>
export default {
  name: "ItemCard",
  props:{
    item: Object,
    category: Number
  },
  data(){
    return{
    }
  },
  computed:{
    iconSrc(){
      let src = './assets/defaultCardIcon.svg';
      if(this.item.src){
        src = this.item.src;
      }
      return src;
    },
    cash(){
      if(this.item.shops) {
        const tempUnsorted = JSON.parse(JSON.stringify(this.item));
        const tempSorted = tempUnsorted.shops.sort((a, b) => b.cashback - a.cashback);
        return tempSorted[0];
      }
      return this.item.cashback;
    }

  }
};
</script>

<style scoped>

.item-container{
  display: inline-flex;
  flex-direction: column;
  width: 30vw ;
  max-width: 200px;
}
.item-container img{
 padding: 0;
  margin: 0;
}
.cashback{
  position: absolute;
  background-color: red;
  left:75%;
  top:0;
}

</style>
