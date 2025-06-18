<script setup>
import { ref } from "vue";

function jumping(turl) {
  window.location.assign(turl)
}
// let Murl = "http://localhost:8080/"
let id = 0;
const items = ref([
  { id: id++, text: "Document", content:"want to learn?", tsrc:"document"},
  { id: id++, text: "Login/Register", content:"want a personal place?", tsrc:"lgrg"},
  { id: id++, text: "ReplayPanel", content:"need replay?", tsrc:"replaypanel"},
  { id: id++, text: "About", content:"curiosity for this and us?", tsrc:"about"}
])

</script>

<template>
  <ul>
    <li v-for="item in items" :key="item.id" @click="jumping(item.tsrc)">
      <h3>{{ item.text }}</h3>
      <p>{{ item.content }}</p>
    </li>
  </ul>
</template>

<style scoped>
  ul{
    /* display: flex; */
    margin-left: 15%;
    margin-right: 15%;
  }
  li{
    margin: 20px;
    list-style-type: none;
    border-radius: 5px;
    font-size: 25px;
    background-color: blanchedalmond;
  }li:hover{
    cursor: pointer;
  }
  h3{
    margin-bottom: 5px;
  }
  p{
    margin-top: 5px;
  }
</style>
