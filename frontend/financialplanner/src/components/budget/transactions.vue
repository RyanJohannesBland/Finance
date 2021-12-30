<template>
  <v-container fluid fill-height>
    <v-row justify="center">
      <v-data-table :headers="headers" :items="desserts" dark>
        <template v-slot:item.spent="{ item }">
          <v-chip :color="getColor(item)" dark>
            {{ item.spent }}
          </v-chip>
        </template>
      </v-data-table>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        {
          text: "Categories",
          align: "start",
          value: "name",
        },
        { text: "Budget", value: "allowance" },
        { text: "This Month", value: "spent" },
        { text: "Remaining", value: "sum" },
      ],
      desserts: [
        {
          name: "Gas",
          allowance: 200,
          spent: 225,
          sum: 24,
        },
        {
          name: "Auto Insurance",
          allowance: 235,
          spent: 235,
          sum: 37,
        },
        {
          name: "Auto Maintenance",
          allowance: 200,
          spent: 16.0,
          sum: 23,
        },
        {
          name: "Groceries",
          allowance: 150,
          spent: 145,
          sum: 67,
        },
        {
          name: "Phone Bill",
          allowance: 65,
          spent: 65,
          sum: 49,
        },
        {
          name: "Experiences",
          allowance: 375,
          spent: 0.0,
          sum: 94,
        },
        {
          name: "Things",
          allowance: 100,
          spent: 0.2,
          sum: 98,
        },
      ],
    };
  },
  methods: {
    getColor(category) {
      if (category.spent > category.allowance) return "green";
      else if (category.spent / category.allowance > 0.85) return "orange";
      else return "red";
    },
  },
};
</script>
