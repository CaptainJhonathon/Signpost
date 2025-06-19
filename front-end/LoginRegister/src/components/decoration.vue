<script setup>

</script>

<template>
  <div id="one">
    <div id="oneimage">
      <img src="../assets/logo.svg" alt="Signpost Logo" id="onelogo">
    </div>
    <div id="oneulbox">
      <ul id="oneul">
        <li>
          <h2 id="onetitle">Signpost</h2>
        </li>
        <li>
          <p id="oneps">Login or Register</p>
        </li>
      </ul>
    </div>



  </div>

</template>

<style scoped>
#one{
  display: flex;
}
#oneimage{
  width: 30%;
  height: inherit;
  display: flex;
  align-items: center;
  justify-content: center;
}
#onelogo {
  width: 22px;
  height: 32px;
}

#oneulbox {
  display: flex;
  width: 60%;
}

#oneul {
  width: 100%;
  padding: 0;
}

#oneul li {
  list-style-type: none;
  margin: auto;
}

#onetitle,
#oneps {
  margin: auto;
  text-align: center;
}
</style>
