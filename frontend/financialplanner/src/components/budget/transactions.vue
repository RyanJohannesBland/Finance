<template>
  <v-container fluid fill-height>
    <v-row justify="center">
      <v-data-table
        :headers="headers"
        :items="transactions"
        dark
        hide-default-footer
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="500px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  light
                  class="mb-2"
                  v-bind="attrs"
                  v-on="on"
                  @click="createItem"
                >
                  New Item
                </v-btn>
              </template>
              <v-card>
                <v-card-title class="text-h5">{{ dialogHeader }}</v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="editedTransaction.date"
                          label="Date"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-select
                          v-model="editedTransaction.category"
                          label="Category"
                          :items="categories"
                          item-text="name"
                          item-value="name"
                        ></v-select>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="editedTransaction.amount"
                          label="Amount"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-btn @click="deleteItem" color="red"> Delete </v-btn>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="dialog = false">
                    Cancel
                  </v-btn>
                  <v-btn color="blue darken-1" text @click="saveItem">OK</v-btn>
                  <v-spacer></v-spacer>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
        </template>
        <template v-slot:item.amount="{ item }">
          <v-chip :color="getColor(item)" dark>
            {{ item.amount }}
          </v-chip>
        </template>
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-1" @click="editItem(item)"
            >mdi-pencil
          </v-icon>
        </template>
      </v-data-table>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      dialogHeader: "",
      headers: [
        { text: "Date", value: "date" },
        { text: "Categories", value: "category" },
        { text: "Amount", value: "amount" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      transactions: [],
      categories: [],
      editedTransaction: {},
      editedIndex: -1,
    };
  },
  methods: {
    getColor(category) {
      if (category.amount > 0) return "green";
      else return "red";
    },
    createItem() {
      this.editedTransaction = {};
      this.editedIndex = -1;
      this.dialogHeader = "Create Transaction";
      this.dialog = true;
    },
    editItem(item) {
      this.editedTransaction = Object.assign({}, item);
      this.editedIndex = this.transactions.indexOf(item);
      this.dialogHeader = "Edit Transaction";
      this.dialog = true;
    },
    deleteItem() {
      this.editedTransaction = { id: this.editedTransaction.id };
    },
    saveItem() {
      // Create new transaction.
      if (this.editedIndex == -1) {
        this.$api
          .post("transactions/", this.editedTransaction)
          .then(() => {
            this.refreshData();
          })
          .catch((error) => {
            console.log(error);
          });
      }
      // Delete a transaction.
      else {
        if (!this.editedTransaction.amount) {
          this.$api
            .delete("transactions/" + this.editedTransaction.id + "/")
            .then(() => {
              this.refreshData();
            });
        }
        // Edit a transaction.
        else {
          this.$api
            .put(
              "transactions/" + this.editedTransaction.id + "/",
              this.editedTransaction
            )
            .then(() => {
              this.refreshData();
            })
            .catch((error) => {
              console.log(error);
            });
        }
      }
      this.dialog = false;
    },
    refreshData() {
      this.$api
        .get("transactions")
        .then((response) => {
          this.transactions = response.data;
        })
        .catch((error) => {
          console.log(error.data);
        });
    },
  },
  beforeMount: function () {
    // Grab Transactions and Categories on load.
    this.$api
      .get("categories")
      .then((response) => {
        this.categories = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
    this.refreshData();
  },
};
</script>
