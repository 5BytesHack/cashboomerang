<template>
    <q-layout view="lHh lpR lFf">
      <q-header elevated class="bg-grey-3 text-grey-14 q-py-md" height-hint="98">
        <q-toolbar>
          <q-toolbar-title>
            <span class="text-h4">Панель администрирования</span>
          </q-toolbar-title>
          <span class="text-h5 q-pr-lg none">{{mail}}</span>
          <q-btn flat dense label="Выйти" style="border-radius: 13px" class="q-mr-xs bg-red q-px-md q-py-xs text-white" />

        </q-toolbar>
      </q-header>

      <q-drawer show-if-above  side="left"  class="bg-grey-14" :width="330">

         <div class="q-pa-md  text-orange-5 shadow-3">
           <q-toolbar-title >
             <div style="display: flex; align-items: center; justify-content: space-between">
               <q-avatar style="margin-bottom: 2px;">
                 <img src="../assets/header/logo.svg" alt="">
               </q-avatar>
               <span class="text-h4 ">Бумеранг-кэш</span>
             </div>
           </q-toolbar-title>
         </div>

          <q-list class="menu-list ">
            <q-item clickable v-ripple class="shadow-3 q-py-lg text-center" v-for="tab in tabs" :key="tab.title" :name="tab.name"
                    @click="current_tab=tab.name" :class="[current_tab == tab.name ? 'white-bg':'text-white']">
              <q-item-section>
                <span class="text-h4">{{tab.title}}</span>
              </q-item-section>
            </q-item>
          </q-list>
      </q-drawer>

      <q-page-container>
        <keep-alive><component :is="check_tab"></component></keep-alive>
      </q-page-container>

    </q-layout>
</template>

<script>
import SetupComp from "components/SetupComp";
import StatisticsComp from "components/StatisticsComp";
import DataComp from "components/DataComp";
export default {
  name: "AdminPanel",
  components:{
    SetupComp,
    StatisticsComp,
    DataComp
  },
  props:{
    email:String,
  },
  data(){
    return{
      tabs:[{name: "settings", title:"Настройка"},{name: "data", title:"Данные"},{name: "statistic", title:"Статистика"}],
      current_tab:"settings",
      mail: "yatsenko_dmitry@mail.ru",
    }
  },
  computed:{
    check_tab:function(){
      if (this.current_tab == "settings") return "SetupComp";
      if (this.current_tab == "data") return "DataComp";
      if (this.current_tab == "statistic") return "StatisticsComp";
      return "SetupComp";
    }
  }
};
</script>

<style scoped>
  .white-bg{
    background-color: white;
    color: #616161;
    box-shadow: 0 0 5px 1px darkgrey;
  }
</style>
