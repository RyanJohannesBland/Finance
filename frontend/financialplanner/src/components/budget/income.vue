<template>
  <data-table
    :headers="headers"
    :items="incomes"
    itemType="Income Stream"
    :vStreams="[]"
    @post="postItem"
    @put="putItem"
    @delete="deleteItem"
  ></data-table>
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
        { text: "Goal", value: "allowance" },
        { text: "Edit", value: "actions", sortable: false, ignore: true },
      ],
      incomes: [],
    };
  },
  methods: {
    postItem(item) {
      this.$api
        .post("categories/", item)
        .then(() => {
          this.refreshCategories();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    putItem(item) {
      this.$api
        .put("categories/" + item.name + "/", item)
        .then(() => {
          this.refreshCategories();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteItem(item) {
      this.$api
        .delete("categories/" + item.name)
        .then(() => {
          this.refreshCategories();
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted: function () {},
};
</script>
