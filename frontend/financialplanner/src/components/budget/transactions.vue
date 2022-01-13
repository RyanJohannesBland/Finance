<template>
  <v-container fluid fill-height>
    <data-table
      :headers="headers"
      :items="transactions"
      itemType="Transaction"
      :vSelects="categories"
      @post="postItem"
      @put="putItem"
      @delete="deleteItem"
    >
      <template v-slot:item.amount="{ item }">
        <v-chip :color="getColor(item)" dark>
          {{ item.amount }}
        </v-chip>
      </template>
    </data-table>
  </v-container>
</template>

<script>
import dataTable from "@/components/data-table.vue";
export default {
  props: ["transactions", "categories"],
  components: {
    "data-table": dataTable,
  },
  data() {
    return {
      headers: [
        { text: "Date", value: "date" },
        { text: "Categories", value: "category" },
        { text: "Amount", value: "amount" },
        { text: "Actions", value: "actions", sortable: false, ignore: true },
      ],
    };
  },
  methods: {
    getColor(category) {
      if (category.amount > 0) return "green";
      else return "red";
    },
    postItem(item) {
      this.$api
        .post("transactions/", item)
        .then(() => {
          this.$emit("reload");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    putItem(item) {
      this.$api
        .put("transactions/" + item.id + "/", item)
        .then(() => {
          this.$emit("reload");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    deleteItem(item) {
      this.$api.delete("transactions/" + item.id + "/").then(() => {
        this.$emit("reload");
      });
    },
  },
};
</script>
