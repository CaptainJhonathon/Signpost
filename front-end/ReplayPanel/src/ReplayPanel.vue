<script setup>
import navigator from './components/navigator.vue';
import statusBar from './components/statusBar.vue';
import platforms from './components/platforms.vue';
import replay from './components/replay.vue';
</script>

<template>
    <h1>Hello,World!</h1>
    <div id="navigator"><navigator></navigator></div>
    <div id="statusBar"><statusBar></statusBar></div>
    <div id="platforms"><platforms></platforms></div>
    <div id="replay"><replay></replay></div>
</template>

<style scoped>
    .navigator{
        
    }
</style>