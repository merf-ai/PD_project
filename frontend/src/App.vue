<template>
  <navbar></navbar>
  <div class="d-flex justify-content-center position-absolute top-50 start-50">
    <div class="" :class="{ 'spinner-grow justify-content-center mt-3': $store.state.isLoading }" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
  <div class="app">
    <router-view />
  </div>

</template>

<script>
import Navbar from "@/components/Navbar";
import axios from "axios";
export default {
  components: {
    Navbar
  },
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.app {
    padding: 20px;
}
</style>
