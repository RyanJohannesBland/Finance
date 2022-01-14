import Vue from "vue";
import Vuex from "vuex";
import api from "../plugins/api.js";

Vue.use(Vuex);

// Store default state for clearing auth details.
const getDefaultState = function () {
  return {
    username: null,
    auth_token: null,
  };
};

const store = new Vuex.Store({
  state: getDefaultState(),
  actions: {
    login: function (context, creds) {
      api
        .post("login/", creds)
        .then((response) => {
          context.commit("login", {
            username: creds.username,
            auth_token: response.data.access,
          });
        })
        .catch((error) => console.log(error));
    },
    logout: function (context) {
      context.commit("logout");
    },
  },
  mutations: {
    login: function (state, payload) {
      state.username = payload.user;
      state.auth_token = payload.auth_token;
    },
    logout: function (state) {
      Object.assign(state, getDefaultState());
    },
  },
});

export default store;
