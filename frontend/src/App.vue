<template>
  <div id="app">
    <router-view />
  </div>
</template>

<!--region script-->
<script>
export default {
  name: 'app',
  data () {
    return {
      activeIndex: this.$route.name,
    }
  }
}
</script>
<!--endregion-->

<!--region style-->
<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}
a {
  text-decoration: none;
}
</style>

<style>
#app {
  width: 100vw;
  height: 100vh;
}
.menuBar {
  width: 100vw;
  max-height: 60px;
  padding-bottom: 1px;
}
.menuItemWrapper {
  display: flex;
}
.imageWrapper {
  width: 100%;
  text-align: right;
  pointer-events: none;
}
.imageItem {
  justify-content: flex-end;
}
img {
  width: auto;
  height: 100%;
  object-fit: contain;
}
</style>
<!--endregion-->
