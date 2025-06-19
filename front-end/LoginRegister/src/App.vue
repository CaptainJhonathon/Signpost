<script setup>
import decoration from './components/decoration.vue';
import LgrgPanel from './components/LgrgPanel.vue';
</script>

<template>
  <div id="windowone">
    <div id="decoration"><decoration></decoration></div>
    <div id="LgrgPanel"><LgrgPanel></LgrgPanel></div>
  </div>
</template>

<style scoped>
  #windowone{
    padding-top: 10%;
    height: 100vh;
    display: block;
    justify-content: center;
    align-items: center;
  }
  #decoration, #LgrgPanel{
    width: 30%;
    border: 2px solid;
    margin: auto;
    height: 200px;
    
  }
  #decoration{
    border-bottom: 0px;
    border-radius: 5px 5px 0 0;
    height: 70px;
  }#LgrgPanel{
    border-radius: 0 0 5px 5px;
  }
  
</style>
