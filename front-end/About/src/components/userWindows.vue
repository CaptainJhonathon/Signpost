<script setup>
// import { ref } from "vue";
function goLogin() {
    window.location.assign("lgrg")
    // remember to add the login url
}
</script>

<template>
    <div id="Interact">
        <button type="button" @click="goLogin">
            Login/Register
        </button>
    </div>
</template>

<style scoped>
    button{
        border: none;
        background-color: inherit;
    }button:hover{
        cursor: pointer;
    }
</style>