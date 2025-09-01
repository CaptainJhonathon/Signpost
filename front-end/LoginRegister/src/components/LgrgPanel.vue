<!-- <script setup>
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
  
</template> -->

<script setup>
import { ref } from 'vue';

const useraccount = ref('');
const userpassword = ref('');
const verifycodeinput = ref('');

// 验证函数
function validateForm() {
  let isValid = true;
  let errorMessage = '';

  // 验证邮箱格式
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(useraccount.value)) {
    errorMessage = '邮箱格式不正确';
    isValid = false;
  }

  // 验证密码长度
  if (userpassword.value.length < 8 || userpassword.value.length > 16) {
    errorMessage = '密码必须为8到16位';
    isValid = false;
  }

  // 验证验证码格式
  const verifyCodeRegex = /^[a-zA-Z0-9]{4}$/;
  if (!verifyCodeRegex.test(verifycodeinput.value)) {
    errorMessage = '验证码必须为4位字母和数字';
    isValid = false;
  }

  if (!isValid) {
    alert(errorMessage);
  }

  return isValid;
}

// 跳转函数
function jumping() {
  if (validateForm()) {
    window.location.assign("home");
  }
}
</script>

<template>
  <form action="post" id="lgrgform">
    <label for="uiaccount">e-mail:</label>
    <input type="text" v-model="useraccount" id="uiaccount"><br>
    <label for="uipassword">password:</label>
    <input type="password" v-model="userpassword" id="uipassword"><br>
    <label for="uiverifycode">verifycode</label>
    <input type="text" v-model="verifycodeinput" id="uiverifycode"><br>
    <img src="../assets/captcha.png" alt="verify code image" id="verifycodeimage"><br>
    <button type="button" id="tbtn" @click="jumping">Login/Register</button>
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
