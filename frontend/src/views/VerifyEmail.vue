<template>
    <div>haha</div>
    <div>Board with prop id: {{ uid }}</div>
    <div>Board with prop id: {{ token }}</div>
  </template>
  
  <script>
  export default {
    computed: {
      uid() {
        return this.$route.params.uid;
      },
      token() {
        return this.$route.params.token;
      }
    },
  };
  </script>