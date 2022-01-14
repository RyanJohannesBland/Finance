<template>
  <v-app app>
    <v-app-bar app dark>
      <v-app-bar-nav-icon
        v-if="$store.state.auth_token"
        @click.stop="drawer = !drawer"
      ></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-toolbar-title>Financial Planning Tool</v-toolbar-title>
      <v-spacer></v-spacer>
      <div v-if="$store.state.auth_token">
        <div>{{ $store.state.username }}</div>
        <v-btn @click="logout">Logout</v-btn>
      </div>
      <div v-else>
        <v-btn @click="dialog = true">Login</v-btn>
        <v-dialog v-model="dialog" absolute>
          <v-card>
            <v-card-title>Login</v-card-title>
            <v-card-text>
              <v-text-field label="Username" v-model="username"></v-text-field>
              <v-text-field label="password" v-model="password"></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-btn @click="login">Submit</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
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
        <router-view class="background:#03f431"></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      dialog: false,
      username: "",
      password: "",
    };
  },
  methods: {
    login() {
      this.$store.dispatch("login", {
        username: this.username,
        password: this.password,
      });
    },
    logout() {
      this.$store.dispatch("logout");
    },
  },
};
</script>
