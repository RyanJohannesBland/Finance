<template>
  <v-container>
    <v-row justify="center">
      <v-data-table :headers="headers" :items="items" dark hide-default-footer>
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-1" @click="openEditDialog(item, 'edit')">
            mdi-pencil
          </v-icon>
          <v-icon small @click="openDeleteDialog(item)"> mdi-delete </v-icon>
        </template>
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
                  @click="openEditDialog({}, 'create')"
                >
                  Create New {{ itemType }}
                </v-btn>
              </template>
              <v-card>
                <v-card-title class="text-h5">
                  {{ itemType }} Editor
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="6" v-for="key of fields" :key="key">
                        <v-select
                          v-if="key in vSelects"
                          v-model="selectedItem[key]"
                          :label="key"
                          :items="vSelects[key].options"
                          :item-text="vSelects[key].pk"
                          :item-value="vSelects[key].pk"
                        ></v-select>
                        <v-text-field
                          v-else
                          v-model="selectedItem[key]"
                          :label="key"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <!-- <v-row>
                      <v-col>
                        <v-text-field
                          v-model="selectedItem"
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
                    </v-row> -->
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="dialog = false">
                    Cancel
                  </v-btn>
                  <v-btn color="blue darken-1" text @click="handleEditing">
                    OK
                  </v-btn>
                  <v-spacer></v-spacer>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
        </template>
        <!-- Magic code that allows me to pass slots from parent through data-table to
        v-data-table. -->
        <template
          v-for="slot in Object.keys($scopedSlots)"
          :slot="slot"
          slot-scope="scope"
        >
          <slot :name="slot" v-bind="scope" />
        </template>
      </v-data-table>
    </v-row>
    <v-dialog v-model="deleteDialog" max-width="500px">
      <v-card>
        <v-card-title class="text-h5">
          Are you sure you want to delete this item?
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="deleteDialog = false">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="deleteItem"> Delete </v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  props: ["headers", "items", "itemType", "vSelects"],
  data() {
    return {
      dialog: false,
      deleteDialog: false,
      selectedItem: {},
      editingMode: "create",
      fields: [],
    };
  },

  methods: {
    openDeleteDialog(item) {
      this.selectedItem = item;
      this.deleteDialog = true;
    },
    openEditDialog(item, mode) {
      this.editingMode = mode;
      this.selectedItem = item;
      this.dialog = true;
    },
    handleEditing() {
      if (this.editingMode === "create") {
        this.$emit("post", this.selectedItem);
      } else {
        this.$emit("put", this.selectedItem);
      }
      this.selectedItem = {};
      this.dialog = false;
    },
    deleteItem() {
      this.$emit("delete", this.selectedItem);
      this.deleteDialog = false;
    },
  },
  mounted: function () {
    this.fields = this.headers.filter((e) => !e.ignore).map((e) => e.value);
    // Raise exceptions in mounted?
    // All items need to have the same fields.
    // Headers should always contain the "Actions" header.
  },
};
</script>
