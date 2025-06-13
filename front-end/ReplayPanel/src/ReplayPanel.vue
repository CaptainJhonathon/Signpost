<script setup>
import navigator from './components/navigator.vue';
import platforms from './components/platforms.vue';
import replay from './components/replay.vue';
</script>

<template>
    <div id="navigator"><navigator></navigator></div>
    <div id="platforms"><platforms></platforms></div>
    <div id="replay"><replay></replay></div>
</template>

<style scoped>
    #navigator{
        background-color: rgb(179, 170, 170);
        display: flex;
        margin: 0 auto;
        position: fixed;
        top: 0px;
        width: 100%;
    }
    #platforms{

    }
</style>