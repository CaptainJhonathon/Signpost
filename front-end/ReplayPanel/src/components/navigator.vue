<script setup>
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
    <h1>this is navigator</h1>
    <ul>
        <li v-for="page in pages" :key="page.id">
            <a :href="page.tsrc">
                {{ page.text }}
            </a>
        </li>
    </ul>
</template>

<style scoped>
    ul{
        list-style-type: none;
        display: flex;
        border-style: solid;
        border-width: 2px;
        padding-left: 20%;
    }
    li{
        margin: 5px;
        border-style: solid;
        border-width: 2px;
    }
</style>