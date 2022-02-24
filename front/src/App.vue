<template>
  <div>
    <Toxicity />
  </div>
</template>

<script>
import Toxicity from "./components/Toxicity.vue";

export default {
  name: "App",
  components: {
    Toxicity,
  },
};
</script>

<style>
#app {
  font-family: 'Roboto', sans-serif;
  text-align: center;
  color: #fff;
  background: #02044a;
}

html, body, #app{
  height: 100%;
}
</style>
