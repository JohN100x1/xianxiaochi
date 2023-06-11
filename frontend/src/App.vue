<template>
  <img width="500" alt="西安小吃徽标" src="./assets/logo.svg">
  <HomePage title="Coming Soon"/>
  <!-- <ul>
    <li>Opening hours: 12:00 - 21:30</li>
  </ul> -->
</template>

<script>
import HomePage from './components/HomePage.vue'

export default {
  name: 'App',
  components: {
    HomePage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
