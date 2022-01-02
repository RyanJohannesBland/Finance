<template>
  <v-container>
    <v-row justify="center">
      <data-table
        :headers="headers"
        :items="categories"
        itemType="Budget Category"
        :vSelects="subcategories"
        @post="postItem"
        @put="putItem"
        @delete="deleteItem"
      >
        <template v-slot:item.spent="{ item }">
          <v-chip :color="getColor(item)" dark>
            {{ item.spent }}
          </v-chip>
        </template>
      </data-table>
    </v-row>
  </v-container>
</template>

<script>
import dataTable from "@/components/data-table.vue";

export default {
  components: {
    "data-table": dataTable,
  },
  data() {
    return {
      headers: [
        {
          text: "Categories",
          align: "start",
          value: "name",
        },
        { text: "Subcategory", value: "subcategory" },
        { text: "Budget", value: "allowance" },
        { text: "This Month", value: "spent" },
        { text: "Remaining", value: "balance" },
        { text: "Edit", value: "actions", sortable: false },
      ],
      categories: [],
      subcategories: [],
    };
  },
  methods: {
    getColor(category) {
      if (category.spent > category.allowance) return "red";
      else if (category.spent / category.allowance > 0.85) return "orange";
      else return "green";
    },
    postItem(item) {
      this.$api
        .post("categories", item)
        .then(() => {
          this.refreshData();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    putItem(item) {
      this.$api
        .put("categories/" + item.name, item)
        .then(() => {
          this.refreshData();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteItem(item) {
      this.$api
        .delete("categories/" + item.name)
        .then(() => {
          this.refreshData();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    refreshData() {
      this.$api
        .get("categories")
        .then((response) => {
          this.categories = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  beforeMount: function () {
    this.refreshData();
    this.$api
      .get("subcategories")
      .then((response) => {
        this.subcategories = {
          subcategory: { pk: "name", options: response.data },
        };
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>
