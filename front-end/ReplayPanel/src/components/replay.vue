<script setup>
import { ref } from 'vue';
import queue from './queue.vue';

const datetime = ref("")

let item_id = 0
const items = ref([
    {id: item_id++, text:"(using form response!)"}
])
</script>

<template>
    <form method="post" id="DT">
        <input type="datetime-local" v-model="datetime">
        <p>datetime input is <strong>{{ datetime }}</strong></p>
        <!-- <input type="submit"> 
         NOTE: make submission automatic
        -->
    </form>

    <ul>
        <li v-for="item in items" :key="item.id">
            {{ item.text }}
        </li>
    </ul>

    <div id="queue"><queue></queue></div>
</template>

<style scoped>
    #DT{
        margin: 4px 4px 4px;
    }
    ul{
        list-style-type: none;
    }
</style>