<template>
  <div class="popup-item-container q-py-xs flex q-mb-sm">
    <div class="info-container q-px-sm">
      <img src="../assets/ItemDefaultIcon.png" alt="" height="65">
    </div>
    <div class="info-container">
      <span class="text-h6">{{name}}</span>
    </div>
    <div class="cash-container q-px-sm">
      <span>{{cash}}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "PopupItem",
  props:{
    src:String,
    name:String,
    cash: String,
  }
};
</script>

<style scoped>
.popup-item-container{
  height: 90px;
  border-bottom: 1px solid gray;
}
.info-container{
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: auto 0;
  ;
}
.cash-container{
  color: red;
  align-self: center;
  flex-grow: 1;
  text-align: end;
}
.cash-container::after{
  content: "%";
}
</style>
