<script setup>
import { ref } from 'vue';

const datetime = ref("")

let item_id = 0
const items = ref([
    {id: item_id++, text:"(using form response!)"}
])
</script>

<template>
    <h1>this is replay</h1>
    <form method="post">
        <input type="datetime-local" v-model="datetime">
        <p>datetime input is <h1>{{ datetime }}</h1></p>
        <!-- <input type="submit"> 
         NOTE: make submission automatic
        -->
    </form>

    <ul>
        <li v-for="item in items" :key="item.id">
            {{ item.text }}
        </li>
    </ul>
</template>

<style scoped>
    ul{
        list-style-type: none;
    }
</style>