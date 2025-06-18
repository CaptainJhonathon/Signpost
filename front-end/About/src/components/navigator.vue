<script setup>
import userWindows from './userWindows.vue';
import { ref } from 'vue';
let id = 0
const pages = ref([
    {id: id++, text:"Home", tsrc:"home"},
    {id: id++, text:"Document", tsrc:"document"},
    {id: id++, text:"ReplayPanel", tsrc:"replaypanel"},
    {id: id++, text:"About", tsrc:"about"}
])
</script>

<template>
    <a href="http://localhost:8080" id="logolink">
        <img src="../assets/logo.svg" alt="Our logo image" id="logo">
    </a>

    <ul>
        <li v-for="page in pages" :key="page.id">
            <a :href="page.tsrc">
                {{ page.text }}
            </a>
        </li>
    </ul>

    <div id="userWindows"><userWindows></userWindows></div>
</template>

<style scoped>
    ul{
        list-style-type: none;
        display: flex;
        padding-left: 6px;
        margin: 2px;
    }
    li{
        margin: 5px;
        margin-right: 15px;
    }
    a{
        color: black;
        text-decoration: none;
    }a:hover{
        cursor: pointer;
        font-style: italic;
    }
    #logo{
        width: 20px;
        height: 35px;
        margin-right: 10px;
    }#logolink{
        margin: 0px;
    }
    #userWindows{
        margin-left: 10px;
        margin-top: 5px;
        margin-bottom: 5px;
        position: fixed;
        right: 5%;
    }
</style>