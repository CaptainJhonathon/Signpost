<script setup>
import navigator from './components/navigator.vue';
import platforms from './components/platforms.vue';
import replay from './components/replay.vue';
</script>

<template>
    <div id="navigator"><navigator></navigator></div>
    <div id="panel">
        <div id="platforms"><platforms></platforms></div>
        <div id="replay"><replay></replay></div>
    </div>
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

    #panel{
        position: static;
        display: flex;
        margin-top: 5%;
    }
    #platforms{
        
        border: 2px solid;
        width: 20%;
        height: 100%;
    }
    #replay{
        
        border: 2px solid;
        width: 80%;
    }
    
</style>