<script setup>
import userWindows from './userWindows.vue';
import { ref } from 'vue';
let id = 0
const pages = ref([
    {id: id++, text:"Home", tsrc:"Home"},
    {id: id++, text:"Document", tsrc:"Document"},
    {id: id++, text:"ReplayPanel", tsrc:"ReplayPanel"},
    {id: id++, text:"About", tsrc:"About"}
])
</script>

<template>
    <img src="../assets/logo.svg" alt="Our logo image" id="logo">

    <ul>
        <li v-for="page in pages" :key="page.id">
            <a :href="page.tsrc">
                {{ page.text }}
            </a>
        </li>
    </ul>

    <div><userWindows></userWindows></div>
</template>

<style scoped>
    ul{
        list-style-type: none;
        display: flex;
        padding-left: 6px;
        margin: 0px;
    }
    li{
        margin: 5px;
        margin-right: 15px;
    }
    #logo{
        width: 20px;
        height: 30px;
    }
</style>