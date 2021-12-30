<template>
  <v-app app>
    <v-app-bar app dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-toolbar-title>Financial Planning Tool</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" dark absolute temporary>
      <v-list>
        <v-list-item @click="$router.push('/budget')">
          <v-list-item-icon>
            <v-icon>mdi-hand-wave</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Budget</v-list-item-title>
        </v-list-item>
        <v-list-item @click="$router.push('/transactions')">
          <v-list-item-icon>
            <v-icon>mdi-egg</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Transactions</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <v-container fluid fill-height class="pa-0 ma-0">
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
    };
  },
};
</script>
