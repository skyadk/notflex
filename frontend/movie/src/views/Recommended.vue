<template>
  <div class="main-back">
    <div class="back"></div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.main-back {
  background: url(../assets/back.png) no-repeat;
  background-size: cover;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-attachment: fixed;
}
.back {
  background: rgba(0, 0, 0, 0.8);
  width: 100%;
  height: 100%;
  margin-top: 5%;
}
</style>
