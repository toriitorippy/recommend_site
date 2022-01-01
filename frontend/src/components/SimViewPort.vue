<template>
  <div class="wrapper">
    <el-card class="box-card">
      <TradeoffWrapper @click="updatePort"/>
    </el-card>
  </div>
</template>

<script>
import TradeoffWrapper from "../charts/tradeoff/TradeoffWrapper";

export default {
  name: "ViewPort",
  components: { TradeoffWrapper },
  methods: {
    updatePort() {
      this.$emit("update")
    }
  }
}

</script>

<style scoped>
  .wrapper {
    text-align: center;
  }
  .box-card {
    display: inline-block;
    width: 90%;
    text-align: center;
  }
</style>