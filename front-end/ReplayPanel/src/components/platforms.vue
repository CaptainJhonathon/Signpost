<script setup>
import { ref } from 'vue';

let id = 0
const platforms = ref([
    {id:id++, text:"WeiBo"},
    {id:id++, text:"(developping)"}
])
</script>

<template>
    <h1>this is platforms</h1>
    <ul>
        <li v-for="platform in platforms" :key="platform.id">
            {{ platform.text }}
        </li>
    </ul>
</template>

<style scoped>
    ul{
        list-style-type: none;
    }
</style>