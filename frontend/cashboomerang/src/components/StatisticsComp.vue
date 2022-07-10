<template>
<div class="container">
  <h4><strong>Популярные товары</strong></h4>
  <div class="row">
    <div class="col-3">
      <item-card :item="items1" :badge_show="false"></item-card>
    </div>
    <div class="col-3">
      <item-card :item="items2" :badge_show="false"></item-card>
    </div>
    <div class="col-3">
      <item-card :item="items3" :badge_show="false"></item-card>
    </div>
    <div class="col-3">
      <item-card :item="items4" :badge_show="false"></item-card>
    </div>
    <div class="col-3">
      <item-card :item="items5" :badge_show="false"></item-card>
    </div>

  </div>
<!--  <h4><strong>Популярные магазины</strong></h4>-->
<!--  <div class="row">-->
<!--    <div class="col-3" v>-->
<!--      <item-card :item="item1" :badge_show="false"></item-card>-->
<!--    </div>-->
<!--  </div>-->
</div>
</template>

<script>
import ItemCard from "components/ItemCard";
export default {
  name: "StatisticsComp",
  components:{
    ItemCard,
  },
  data(){
    return{
      items1:{
        name: "Гречневая каша",
        src: 'assets/defaultCardIcon.svg'
      },
      items2:{
        name: "Шоколад Alpen Gold",
        src: 'assets/defaultCardIcon.svg'
      },
      items3:{
        name: "Яблоки",
        src: 'assets/defaultCardIcon.svg'
      },
      items4:{
        name: "Бигмак",
        src: 'assets/defaultCardIcon.svg'
      },
      items5:{
        name: "Молоко",
        src: 'assets/defaultCardIcon.svg'
      },
    }
  }
};
</script>

<style scoped>

</style>
