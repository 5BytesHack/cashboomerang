<template>
  <div class="bg-grey-14">
    <div class="container">
      <q-toolbar class="q-pt-sm row items-start q-px-md text-white">
        <q-avatar size="3.1rem">
          <img src="../assets/header/logo.svg" @click="backToMainScreen">
        </q-avatar>

        <q-toolbar-title class="xs-hide">CashBoomerang</q-toolbar-title>
        <q-space></q-space>
        <div class="column">
          <q-btn style="margin-bottom: 0.1rem;" class="q-pa-1" flat dense>
            <img style="width:1.4rem" src="../assets/header/userLogo.svg"/>
          </q-btn>
          <q-badge color="red q-mb-sm">ID: {{$store.state.userId}}</q-badge>
        </div>
      </q-toolbar>
    </div>
  </div>
  <div class="q-my-md container">
    <div class="q-mx-lg">
      <div class="">
        <q-card class="my-card shadow-5 q-mb-md">
          <q-img src="../assets/header/cards/BankCard.svg"></q-img>
        </q-card>
      </div>
      <div class="q-mb-sm text-grey-14 text-center">
        <span class="text-h4"><strong>История покупок</strong></span>
      </div>
      <div class="">
        <q-list bordered style="border-radius: 20px" class="accordion">
          <q-expansion-item
            group="somegroup"
            label="Чек №"
            header-class="text-grey-14"
            class="accordion-item"
          >
            <q-card class="">
              <q-card-section>
                <q-table
                  title="Пятерочка"
                  :rows="rows"
                  :columns="columns"
                  row-key="name"
                  class="shadow-0 table"
                  hide-bottom
                />
              </q-card-section>
            </q-card>
          </q-expansion-item>
          <q-separator />
        </q-list>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserProfile",
  props:{
    tickets:null,
  },
  data(){
    return{
      rows:[
        {
          name:"Огурцы",
          price: "2000",
        }
      ],
      columns: [
        {
          name: 'name',
          required: true,
          label: 'Название товара',
          align: 'left',
          field: row => row.name,
          format: val => `${val}`,
          sortable: true
        },
        { name: 'price', align: 'center', label: 'Цена', field: 'price', sortable: true },
      ],
    }
  },
  computed:{
    rout_str: function() {
      return "profile/" + this.$store.state.userId;
    }
  },
  methods:{
    backToMainScreen(){
      this.$router.push("/");
    }
  }
};
</script>

<style scoped>
.my-card{
  position: relative;
  border-radius: 20px;
  max-width: 700px;
  margin-left: auto;
  margin-right:auto;
  perspective: 200px;
  transition-duration: 1s;
}
/*.my-card:hover{*/
/*  transform: rotate3d(0, 1, 0, 180deg)*/

/*}*/

.accordion{
  max-width: 700px;
  margin-left: auto;
  margin-right:auto;
}
.accordion-item{
  font-size: 1.2rem;
  font-weight: bold;
}

</style>
