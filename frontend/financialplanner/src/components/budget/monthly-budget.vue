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
        <template v-slot:footer>
          <v-toolbar flat>
            <v-dialog v-model="dialog" max-width="500px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  light
                  class="mb-2"
                  v-bind="attrs"
                  v-on="on"
                  @click="dialog = true"
                >
                  New Subcategory
                </v-btn>
              </template>
              <v-card>
                <v-card-title>Create New Subcategory</v-card-title>
                <v-card-text>
                  <v-text-field
                    v-model="subcategoryName"
                    label="Name"
                  ></v-text-field>
                </v-card-text>
                <v-card-actions>
                  <v-btn @click="createSubcategory">Create</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
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
        { text: "This Month", value: "spent", ignore: true },
        { text: "Remaining", value: "balance" },
        { text: "Edit", value: "actions", sortable: false, ignore: true },
      ],
      categories: [],
      subcategories: [],
      subcategoryName: "",
      dialog: false,
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
    refreshCategories() {
      this.$api
        .get("categories")
        .then((response) => {
          this.categories = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    refreshSubcategories() {
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
    createSubcategory() {
      this.$api
        .post("subcategories/", { name: this.subcategoryName })
        .then(() => {
          this.refreshSubcategories();
          this.dialog = false;
        })
        .catch((error) => console.log(error));
    },
  },
  beforeMount: function () {
    this.refreshCategories();
    this.refreshSubcategories();
  },
};
</script>
