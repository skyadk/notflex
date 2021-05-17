<template>
  <div class="h4 ml-10 pt-3 mb-4 text">{{ text }}</div>
</template>

<script>
export default {
  props: {
    text: String,
  },
};
</script>

<style scoped>
.text {
  color: #fff;
  font-size: 1.5rem;
  font-weight: 1000;
}
</style>
