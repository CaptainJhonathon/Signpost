<script setup>
import navigator from './components/navigator.vue';
import about from './components/about.vue';
</script>

<template>
  <div id="navigator"><navigator></navigator></div>
  <div id="about"><about></about></div>
</template>

<style scoped>
  #navigator{
    background-color: rgb(179, 170, 170);
    display: flex;
    margin: 0 auto;
    position: fixed;
    top: 0px;
    width: 100%;
  }
  #about{
    margin-top: 5%;
  }
</style>
