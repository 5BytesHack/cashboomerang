<template>
<div class="q-my-md container">
  <div class="q-mx-lg">
    <q-card class="my-card shadow-5 q-mb-md">
      <q-img src="../assets/header/cards/BankCard.svg"></q-img>
    </q-card>
    <div class="q-mb-sm text-grey-14">
      <span class="text-h4"><strong>ID</strong></span>

      <span class="text-h4"><strong>{{id}}</strong></span>
    </div>
    <div class="q-mb-sm text-grey-14">
      <span class="text-h4"><strong>История покупок</strong></span>
    </div>
    <div class="">
      <q-list>
        <q-expansion-item
          group="somegroup"
          icon="explore"
          label="First"
          default-opened
          header-class="text-primary"
        >
          <q-card>
            <q-card-section>

            </q-card-section>
          </q-card>
        </q-expansion-item>

        <q-separator />

        <q-expansion-item group="somegroup" icon="perm_identity" label="Second" header-class="text-teal">
          <q-card>
            <q-card-section>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
              commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
              eveniet doloribus ullam aliquid.
            </q-card-section>
          </q-card>
        </q-expansion-item>

        <q-separator />

        <q-expansion-item group="somegroup" icon="shopping_cart" label="Third" header-class="text-purple">
          <q-card>
            <q-card-section>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
              commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
              eveniet doloribus ullam aliquid.
            </q-card-section>
          </q-card>
        </q-expansion-item>

        <q-separator />

        <q-expansion-item
          group="somegroup"
          icon="bluetooth"
          label="Fourth"
          header-class="bg-teal text-white"
          expand-icon-class="text-white"
        >
          <q-card class="bg-teal-2">
            <q-card-section>
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, eius reprehenderit eos corrupti
              commodi magni quaerat ex numquam, dolorum officiis modi facere maiores architecto suscipit iste
              eveniet doloribus ullam aliquid.
            </q-card-section>
          </q-card>
        </q-expansion-item>
      </q-list>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "UserProfile",
  props:{
    userid: String,
  },
  data(){
    return{
    id: this.userid,
    }
  }
};
</script>

<style scoped>
.my-card{
  border-radius: 20px;
}
</style>
