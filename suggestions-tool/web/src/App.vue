<template>
  <div id="app">
    <h2 style="line-height:3px">GAZEBO DOCUMENTATION INDEX</h2>
    <h3>BITBUCKET ISSUE TRACKER</h3>
    <br>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 60%;
  margin: 0 auto;
  color: #2c3e50;
  margin-top: 60px;
}

h3 {
  color: rgb(32, 82, 158);
}
</style>
