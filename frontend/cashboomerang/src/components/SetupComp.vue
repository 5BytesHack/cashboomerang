<template>
  <div class="container">
    <div class="row" style="border-bottom: 1px solid #616161">
      <div class="col-2">
        <h5 class="header"></h5>
      </div>
      <div class="col-8">
        <h5 class="header"><strong>Магазины</strong></h5>
      </div>
      <div class="col-2">
        <h5 class="header"><strong>Кэшбэк</strong></h5>
      </div>
    </div>
    <q-form class="my-table q-mb-lg">
      <div class="row q-py-md" style="border-bottom: 1px dotted #616161">
        <div class="col-2 text-center">
          <input type="checkbox" style="height: 25px; width: 25px;" >
        </div>
        <div class="col-8">
          <span class="text-h6">Пятерочка</span>
        </div>
        <div class="col-2">
          <input type="text" style="height: 25px; ">
        </div>
      </div>
      <q-btn type="submit" color="red" class="q-px-lg q-py-sm q-mt-lg" style="border-radius: 13px;">Изменить</q-btn>
    </q-form>

  </div>
</template>

<script>
export default {
  name: "SetupComp",
  data(){
    return{
      rows:[
        {
          name:"Пятерочка",
          cashback: "2000",
        }],
        columns: [{
          name: 'name',
          required: true,
          label: 'Название магазина',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
      { name: 'cashback', align: 'center', label: 'Кэшбэк', field: 'cashback', sortable: true },],
    }
  }
};
</script>

<style scoped>
  .my-table{

  }
  .header{
    margin-bottom: 0;
  }
</style>
