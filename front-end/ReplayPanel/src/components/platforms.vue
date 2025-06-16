<script setup>
import { ref } from 'vue';

function postPlatform(neededPlatform){
    fetch('https://localhost:8080/Data', {
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({
            pltfm: neededPlatform
        })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
}

let id = 0
const platforms = ref([
    {id:id++, text:"WeiBo", url:"WeiBo"},
    {id:id++, text:"developping", url:"developping"}
])

</script>

<template>
    <ul>
        <li v-for="platform in platforms" :key="platform.id">
            <button type="button" @click="postPlatform">
                {{ platform.text }}
            </button>
        </li>
    </ul>
</template>

<style scoped>
    ul{
        list-style-type: disc;
    }

    button{
        background-color: inherit;
        border: none;
        font-size: 15px;
    }button:hover{
        cursor: pointer;
        font-style: oblique;
    }
</style>