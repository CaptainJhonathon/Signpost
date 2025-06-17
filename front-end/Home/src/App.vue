<script setup>
import { ref } from "vue";

function jumping(turl) {
  window.location.assign(turl)
}
let Murl = "http://localhost:8080/"
let id = 0;
const items = ref([
  { id: id++, text: "Document", tsrc:Murl+"document"},
  { id: id++, text: "Login/Register", tsrc:Murl+"lgrg"},
  { id: id++, text: "ReplayPanel", tsrc:Murl+"replaypanel"},
  { id: id++, text: "About", tsrc:Murl+"about"}
])

</script>

<template>
  <ul>
    <li v-for="item in items" :key="item.id" @click="jumping(item.tsrc)">
      {{ item.text }}
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
</style>
