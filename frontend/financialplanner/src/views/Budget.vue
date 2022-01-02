<template>
  <v-row style="height: 100%">
    <v-tabs grow dark>
      <v-tab v-for="item in items" :key="item.id" ripple>
        <v-icon>{{ item.icon }}</v-icon>
        <div class="px-2">{{ item.name }}</div>
      </v-tab>
      <v-tab-item>
        <v-container>
          <transactions></transactions>
        </v-container>
      </v-tab-item>
      <v-tab-item>
        <v-container>
          <monthly-budget></monthly-budget>
        </v-container>
      </v-tab-item>
      <v-tab-item>
        <v-container>
          <income></income>
        </v-container>
      </v-tab-item>
    </v-tabs>
  </v-row>
</template>

<script>
import transactions from "@/components/budget/transactions.vue";
import monthlyBudget from "@/components/budget/monthly-budget.vue";
import income from "@/components/budget/income.vue";

export default {
  components: {
    transactions: transactions,
    "monthly-budget": monthlyBudget,
    income: income,
  },
  data: function () {
    return {
      items: [
        {
          name: "Transactions",
          icon: "mdi-home",
          id: 0,
        },
        {
          name: "Monthly Budget",
          icon: "mdi-aspect-ratio",
          id: 1,
        },
        {
          name: "Income Statistics",
          icon: "mdi-aspect-ratio",
          id: 2,
        },
      ],
    };
  },
};
</script>
