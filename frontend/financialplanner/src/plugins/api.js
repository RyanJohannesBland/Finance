import axios from "axios";
import store from "../store/index.js";

const instance = axios.create({
  baseURL: "http://localhost:8000/",
  timeout: 100000,
});

// Add a request interceptor
instance.interceptors.request.use(function (config) {
  const token = store.state.auth_token;
  config.headers.Authorization = `Bearer ${token}`;

  return config;
});

export default instance;
