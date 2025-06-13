<script setup>
import { ref } from "vue";
function goLogin() {
    window.location.assign("")
    // remember to add the login url
}
</script>

<template>
    <h1>this is userWindows</h1>
    <div id="userIcon"></div>
    <div id="Interact">
        <button type="button" @click="goLogin">
            Login/Register
        </button>
    </div>
</template>

<style scoped>

</style>