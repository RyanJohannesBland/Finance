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
                        <v-text-field
                          v-model="editedTransaction.category"
                          label="Category"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col>
                        <v-text-field
                          v-model="editedTransaction.spent"
                          label="Spent"
                        ></v-text-field>
                      </v-col>
                      <v-col>
                        <v-btn @click="editedTransaction = {}" color="red">
                          Delete
                        </v-btn>
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
        <template v-slot:item.spent="{ item }">
          <v-chip :color="getColor(item)" dark>
            {{ item.spent }}
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
        { text: "Spent", value: "spent" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      transactions: [
        {
          category: "Gas",
          date: "12/10/2021",
          spent: -225,
        },
        {
          category: "Salary",
          date: "12/12/2021",
          spent: 235,
        },
        {
          category: "Auto Maintenance",
          date: "12/14/2021",
          spent: -16.0,
        },
        {
          category: "Groceries",
          date: "12/15/2021",
          spent: -145,
        },
        {
          category: "Phone Bill",
          date: "12/15/2021",
          spent: -65,
        },
        {
          category: "Experiences",
          date: "12/19/201",
          spent: -100,
        },
        {
          category: "Pocket Change",
          date: "12/19/2021",
          spent: 0.2,
        },
      ],
      editedTransaction: {},
      editedIndex: -1,
    };
  },
  methods: {
    getColor(category) {
      if (category.spent > 0) return "green";
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
    saveItem() {
      if (this.editedIndex == -1) {
        this.transactions.push(this.editedTransaction);
      } else {
        if (!this.editedTransaction.spent) {
          this.transactions.splice(this.editedIndex, 1);
        } else {
          Object.assign(
            this.transactions[this.editedIndex],
            this.editedTransaction
          );
        }
      }
      this.dialog = false;
    },
  },
};
</script>
