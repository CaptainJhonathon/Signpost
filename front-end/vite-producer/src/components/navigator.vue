<script setup>
import { ref } from 'vue';
let id = 0
const pages = ref([
    {id: id++, text:"Home"},
    {id: id++, text:"Document"},
    {id: id++, text:"ReplayPanel"},
    {id: id++, text:"PersonalInfo"},
    {id: id++, text:"Home"}
])
</script>

<template>
    <h1>this is navigator</h1>
    <ul>
        <li v-for="page in pages" :key="page.id">
            {{ page.text }}
        </li>
    </ul>
</template>

<style scoped>
    ul{
        list-style-type: none;
    }
</style>