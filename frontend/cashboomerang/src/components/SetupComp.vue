<template>
  <div class="container">
    <q-table
      title="Пятерочка"
      :rows="rows"
      :columns="columns"
      row-key="name"
      class="shadow-0 table"
      hide-bottom
    />
  </div>
</template>

<script>
export default {
  name: "SetupComp",
  data(){
    return{
      rows:[
        {
          name:"Огурцы",
          price: "2000",
        }],
        columns: [{
          name: 'name',
          required: true,
          label: 'Название товара',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
      { name: 'price', align: 'center', label: 'Цена товара', field: 'price', sortable: true },],
    }
  }
};
</script>

<style scoped>

</style>
