<template>
  <div>
    <h2 class="team text-left">ATM_zip</h2>
    <div class="hello">
      <h1>KOKOSUMU</h1>
      <div class="box"></div>
      <p>住む地域レコメンドアプリ</p>
      <p>あなた嗜好に合わせて住みごごちのいい街を紹介します！</p>
      <div class="box"></div>
      <el-button plain type="primary" round v-on:click="begin()">Start</el-button>
    </div>
    <div class="box"></div>
    <img class="img" src="../assets/images/undraw_our_neighborhood_ya1h.png" style="width: 30%"  />
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods:{
    begin () {
      this.$router.push({
        name: 'example',
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.team{
  margin-top: 20px;
  margin-left:20px;
  color: #409EFF;
  font-family: "PingFang SC";
}

.begin {
  height: 100%;
}
.box {
  height:15px;
}
.hello {
  height: 10%
}

h1 {
  margin: 40px 0 0;
  color: #409EFF;
  font-family: "PingFang SC";
  font-size: 80px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

</style>
