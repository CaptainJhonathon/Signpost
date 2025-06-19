<script setup>
function jumping(){
  window.location.assign("home")
}
</script>

<template>
  <form action="post" id="lgrgform">
    <label for="uiaccount">nickname:</label>
    <input type="text" v-model="useraccount" id="uiaccount"><br>
    <label for="uipassword">password:</label>
    <input type="password" v-model="userpassword" id="uipassword"><br>
    <label for="uiverifycode">verifycode</label>
    <input type="text" v-model="verifycodeinput" id="uiverifycode"><br>
    <img src="../assets/captcha.png" alt="verify code image" id="verifycodeimage"><br>
    <button type="submit" id="tbtn" @click="jumping()">Login/Register</button>
  </form>
  
</template>

<style scoped>
  #lgrgform{
    padding-left: 10px;
  }
  form input{
    margin: 5px;
    width: 50%;

  }
  #verifycodeimage{
    width: 30%;
  }
  #tbtn{
    margin: auto;
    background-color: inherit;
  }#tbtn:hover{
    cursor: pointer;
  }
  
</style>
