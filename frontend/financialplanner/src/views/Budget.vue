<template>
  <v-row style="height: 100%">
    <v-tabs grow dark>
      <v-tab v-for="item in items" :key="item.id" ripple>
        <v-icon>{{ item.icon }}</v-icon>
        <div class="px-2">{{ item.name }}</div>
      </v-tab>
      <v-tab-item>
        <v-container>
          <transactions
            :transactions="transactions"
            :categories="categories_options"
            @reload="
              loadTransactions();
              loadCategories();
            "
          ></transactions>
        </v-container>
      </v-tab-item>
      <v-tab-item>
        <v-container>
          <monthly-budget
            :categories="categories"
            :subcategories="subcategories_options"
            @reload="
              loadSubCategories();
              loadSubCategories();
            "
          ></monthly-budget>
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
      transactions: [],
      categories: [],
      subcategories: [],
      categories_options: [],
      subcategories_options: [],
    };
  },
  methods: {
    loadCategories() {
      this.$api
        .get("categories/")
        .then((response) => {
          this.categories = response.data;
          this.categories_options = {
            category: { pk: "name", options: response.data },
          };
        })
        .catch((error) => {
          console.log(error);
        });
    },
    loadSubCategories() {
      this.$api
        .get("subcategories")
        .then((response) => {
          this.subcategories = response.data;
          this.subcategories_options = {
            subcategory: { pk: "name", options: response.data },
          };
        })
        .catch((error) => {
          console.log(error);
        });
    },
    loadTransactions() {
      this.$api
        .get("transactions")
        .then((response) => {
          this.transactions = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted: function () {
    this.loadCategories();
    this.loadTransactions();
    this.loadSubCategories();
  },
};
</script>
