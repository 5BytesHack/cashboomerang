<template>
  <div class="category-header text-grey-14 q-mb-md">
    <span >{{title}}</span>
  </div>
  <div class="">
    <item-card v-for="item in items" :key="item.name" :item="item"></item-card>
  </div>
</template>

<script>
import itemCard from "components/ItemCard";
export default {
  name: "GroupCard",
  components:{
    itemCard,
  },
  props:{
    title: String,
    link: String,
    items: Array,
  },
  data(){
    return{

    }
  }
};
</script>

<style scoped>
.category-header{
  font-size: 1.2rem;
  font-weight: 700;
  border-bottom: 1px solid grey;

}
</style>
