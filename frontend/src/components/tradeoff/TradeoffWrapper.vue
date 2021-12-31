<template>
    <TradeoffScatter
        ref ="chart"
        v-if="loaded"
        :chartdata="chartdata"
        :options="options"
        style="height: 300px"/>
  <div v-else v-loading="true" style="height: 100%">
  </div>
</template>

<script>
import axios from "axios";
import { API_BASE_URI } from "../../../../util/const";

import TradeoffScatter from "./TradeoffScatter";
import { store } from '../../../stores'


export default {
  name: "tradeoff",
  components : { TradeoffScatter },
  data: ()=> ({
    loaded: false,
    chartdata: null,
    options: null,
  }),
  computed: {
    getchartdata() {
      return this.$store.state.scatterChartData.datasets[1].data;
    },
    getchartdatafake() {
      return this.$store.state.scatterChartData.datasets[0].backgroundColor;
    }
  },
  watch: {
    getchartdata() {
      this.$refs.chart.update_render()
    },
    getchartdatafake() {
      this.$refs.chart.update_render()
    }
  },
  async mounted () {
    this.loaded = false
    const self = this;
    try {
      this.chartdata = this.$store.state.scatterChartData;
      const selfComponent = this;
      this.options = {
        scales: {
          xAxes: [{
            display: true,
            scaleLabel: {
              display: true,
              labelString: "年間平均コスト[円/kw]",
            }
          }],
          yAxes: [{
            display: true,
            scaleLabel: {
              display: true,
              labelString: "二酸化炭素排出量[g-CO2]",
            }
          }],
        },
        responsive: true,
        maintainAspectRatio: false,
        onClick: function(evt, entries) {

          if (entries.length === 1) { // バックグラウンドでないことの確認
            selfComponent.$message({
              message: '相対取引比率が反映されました',
              type: "success",
              showClose: true,
              duration: 3000,
            });

            if (entries[0]._datasetIndex === 0) { //dataset ふたつ目になにもない時
              const position = entries[0]._index;

              const path = API_BASE_URI + '/get_aitai_data' + '/' + String(position)
              axios.get(path).then(res => {
                const data = res.data;
                const newSliderValues = {
                  aitai_0: data.aitai_0,
                  aitai_1: data.aitai_1,
                  aitai_2: data.aitai_2,
                  aitai_3: data.aitai_3,
                }
                store.commit('mutateSliderValues', newSliderValues);
                self.$emit("click")
              })
            } else {
              const position = entries[0]._index;
              console.log(selfComponent.$store.state.aitaiPlotData.data)
              const newSliderValues = selfComponent.$store.state.aitaiPlotData.data[position]
              store.commit('mutateSliderValues', newSliderValues);
              self.$emit("click")
            }
          } else {
              console.log("You selected the background!");
          }
        }
      };
      this.loaded = true;
    } catch (e) {
      console.log(e)
    }
  }
}
</script>

<style scoped>

</style>