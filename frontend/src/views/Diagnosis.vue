<template>
  <b-container>
    <!--参考サイト：http://work2work.work/diagnosis/-->
    <div id="Diagnosis" class="Diagnosis">
      <h2 class="team text-left">KOKOSUMU</h2>
      <div class="menubox" v-bind:class="nemu_active">
        <div>
        <el-card class="box-card">
          <div class="menuItem" key="1" v-if="current_num == 0">
              <div class="menuttl">
                <span class="txt">Q1.通勤通学エリアはどこですか？</span>
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[0]" placeholder="Select">
                  <el-option
                    v-for="item in options[0]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_city_driver_re_0x5e.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="2" v-if="current_num == 1">
              <div class="menuttl">
                <span class="txt">Q2.世帯年収はいくらですか？</span>
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[1]" placeholder="Select">
                  <el-option
                    v-for="item in options[1]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_Savings_re_eq4w.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="3" v-if="current_num == 2">
              <div class="menuttl">
                <span class="txt">Q3.ご職業はなんですか？</span>
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[2]" placeholder="Select">
                  <el-option
                    v-for="item in options[2]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_Updated_resume_re_q1or.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="4" v-if="current_num == 3">
              <div class="menuttl">
                <span class="txt">Q4.希望の住宅の大きさは？</span>
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[3]" placeholder="Select">
                  <el-option
                    v-for="item in options[3]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_houses3_xwf7.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="5" v-if="current_num == 4">
              <div class="menuttl">
                <span class="txt">Q5.所有資産は？</span>
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[4]" placeholder="Select">
                  <el-option
                    v-for="item in options[4]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_Vault_re_s4my.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="6" v-if="current_num == 5">
              <div class="menuttl">
                <span class="txt">Q6.個人年収は？</span>
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[5]" placeholder="Select">
                  <el-option
                    v-for="item in options[5]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_personal_finance_tqcd.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="7" v-if="current_num == 6">
              <div class="menuttl">
                <span class="txt">Q7.お子さんはいますか？</span>
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[6]" placeholder="Select">
                  <el-option
                    v-for="item in options[6]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_doll_play_evbw.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="8" v-if="current_num == 7">
              <div class="menuttl">
                <span class="txt"
                  >Q8.家族と過ごす時間をなるべく多くしたい？</span
                >
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[7]" placeholder="Select">
                  <el-option
                    v-for="item in options[7]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_Chilling_re_4iq9.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="9" v-if="current_num == 8">
              <div class="menuttl">
                <span class="txt">Q9.休みの日には家族そろって出かける？</span>
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[8]" placeholder="Select">
                  <el-option
                    v-for="item in options[8]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_Outdoor_adventure_re_j3b7.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="10" v-if="current_num == 9">
              <div class="menuttl">
                <span class="txt"
                  >Q10.休日にはそろって出かけるような、仲の良い家族が望ましい？</span
                >
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[9]" placeholder="Select">
                  <el-option
                    v-for="item in options[9]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_fatherhood_7i19.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="11" v-if="current_num == 10">
              <div class="menuttl">
                <span class="txt">Q11.希望の家賃額は？</span>
              </div>
              <div class="menuRadio">
                <el-input
                  placeholder="万円"
                  v-model.number="answer[10]"
                  type="number"
                  style="width: 200px"
                ></el-input>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_Site_stats_re_ejgy.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>

          <div class="menuItem" key="12" v-if="current_num == 11">
              <div class="menuttl">
                <span class="txt">Q12.希望の間取りは？</span>
              </div>
              <div class="menuRadio">
                <el-select v-model="answer[11]" placeholder="Select">
                  <el-option
                    v-for="item in options[11]"
                    :key="item"
                    :label="item"
                    :value="item"
                  >
                  </el-option>
                </el-select>
                <label>
                  <el-button plain v-on:click="next()">決定</el-button>
                </label>
              </div>
              <img
                class="img"
                src="../assets/images/undraw_select_house_qbag.png"
                style="display: block; margin: auto; width: 50%"
              />
          </div>
          </el-card>
        </div>
      </div>
      <div class="result" v-bind:class="result_active">
        <div class="box"></div>
        <!--<div class="menuttl">
        <span class="txt">あなたの住みやすい街は...</span>
      </div>
      <h1>{{ result1 }}</h1>
      <h2>{{ result2 }}</h2>
      <h3>{{ result3 }}</h3>-->
        <el-row>
          <el-col :span="10">
            <h3>住みやすい街を</h3>
            <h3>チェックしましょう</h3>
            <img
              class="img"
              src="../assets/images/undraw_Ordinary_day_re_v5hy.png"
              style="width: 100%"
            />
            <div class="box"></div>
            <el-button plain type="primary" v-on:click="downloadCSV">
              ダウンロード
            </el-button>
            <div class="box"></div>
          </el-col>
          <el-col :span="10">
            <TradeoffScatter
              :chart-data="datacollection"
              :options="scatter_options"
            ></TradeoffScatter>
          </el-col>
        </el-row>
        <div class="box"></div>
        <el-button plain type="primary" round v-on:click="restart()"
          >戻る</el-button
        >
        <div class="box"></div>
      </div>
    </div>
  </b-container>
</template>

<script>
import axios from 'axios'
import TradeoffScatter from '../components/tradeoff/TradeoffScatter'
import {API_BASE_URI} from '../../util/const.js'

export default {
  name: 'Diagnosis',
  props: {
    msg: String
  },
  components: {
    TradeoffScatter
  },
  data() {
    return {
      items: [],
      answer: [],
      result: { 0: { area: '港区' }, 1: { area: '港区' }, 2: { area: '港区' } },
      result1: '',
      result2: '',
      result3: '',
      current_num: 0,
      nemu_active: '',
      result_active: '__hide',
      datacollection: null,
      scatter_options: null,
      // 選択肢を列挙
      options: [
        [
          '千代田区',
          '中央区',
          '港区',
          '新宿区',
          '文京区',
          '台東区',
          '墨田区',
          '江東区',
          '品川区',
          '目黒区',
          '大田区',
          '世田谷区',
          '渋谷区',
          '中野区',
          '杉並区',
          '豊島区',
          '北区',
          '荒川区',
          '板橋区',
          '練馬区',
          '足立区',
          '葛飾区',
          '江戸川区',
          'その他の東京都（市町村部）',
          '横浜市',
          '川崎市',
          'その他の神奈川県',
          '千葉市',
          'その他の千葉県',
          'さいたま市',
          'その他の埼玉県',
          '水戸市',
          'その他の茨城県',
          '宇都宮市',
          'その他の栃木県',
          '前橋市',
          '高崎市',
          'その他の群馬県',
          '不明'
        ],
        [
          '200万円未満(150)',
          '200～300万円未満(250)',
          '300～400万円未満(350)',
          '400～500万円未満(450)',
          '500～600万円未満(550)',
          '600～700万円未満(650)',
          '700～800万円未満(750)',
          '800～900万円未満(850)',
          '900～1,000万円未満(950)',
          '1,000～1,200万円未満(1100)',
          '1,200～1,500万円未満(1350)',
          '1,500～2,000万円未満(1750)',
          '2,000～3,000万円未満(2500)',
          '3,000万円以上(3000)',
          '収入はない(0)',
          '無回答・不明'
        ],
        [
          '事務職',
          '技術職',
          'サービス職・販売職',
          '労務職',
          '管理職',
          '役員・理事',
          '専門職・自由業',
          '商工・自営業',
          '農林水産業',
          '高校生',
          '大学生・大学院生',
          '専業主婦・主夫',
          '年金受給者',
          '無職',
          'その他',
          '不明'
        ],
        [
          '15坪未満（約50m2未満）',
          '15～20坪未満（約50～65m2未満）',
          '20～25坪未満（約65～80m2未満）',
          '25～30坪未満（約80～100m2未満）',
          '30～35坪未満（約100～115m2未満）',
          '35～40坪未満（約115～130m2未満）',
          '40～45坪未満（約130～150m2未満）',
          '45～50坪未満（約150～165m2未満）',
          '50坪以上（約165m2以上）',
          '分からない',
          '不明'
        ],
        [
          '100万円未満(50)',
          '100～400万円未満(250)',
          '400～800万円未満(600)',
          '800～1,000万円未満(900)',
          '1,000～1,500万円未満(1250)',
          '1,500～2,000万円未満(1750)',
          '2,000～3,000万円未満(2500)',
          '3,000～5,000万円未満(4000)',
          '5,000～7,000万円未満(6000)',
          '7,000～1億円未満(8500)',
          '1億円以上(10000)',
          '無回答・不明'
        ],
        [
          '200万円未満(150)',
          '200～300万円未満(250)',
          '300～400万円未満(350)',
          '400～500万円未満(450)',
          '500～600万円未満(550)',
          '600～700万円未満(650)',
          '700～800万円未満(750)',
          '800～900万円未満(850)',
          '900～1,000万円未満(950)',
          '1,000～1,200万円未満(1100)',
          '1,200～1,500万円未満(1350)',
          '1,500～2,000万円未満(1750)',
          '2,000～3,000万円未満(2500)',
          '3,000万円以上(3000)',
          '収入はない(0)',
          '無回答・不明'
        ],
        [
          '0～3歳児有',
          '0歳～未就学児有',
          '小学生以下の子ども有',
          '小学生の子ども有',
          '中・高校生の子ども有',
          '大学生・専門学校生・大学院生の子ども有',
          '未婚の社会人・無職・既婚の子ども有',
          'これらの人はいない',
          '不明'
        ],
        [
          '非常にあてはまる',
          'ややあてはまる',
          'あまりあてはまらない',
          '全くあてはまらない',
          '不明'
        ],
        [
          '非常にあてはまる',
          'ややあてはまる',
          'あまりあてはまらない',
          '全くあてはまらない',
          '不明'
        ],
        [
          '非常にあてはまる',
          'ややあてはまる',
          'あまりあてはまらない',
          '全くあてはまらない',
          '不明'
        ],
        [],
        ['ワンルーム', '1K/1DK', '1LDK/2K/2DK', '2LDK/3K/3DK', '3LDK/4K']
      ]
    }
  },
  watch: {
    result_num: function(n, o) {
      print(n, o)
    }
  },
  created: function() {
    var _t = this
    setTimeout(function() {
      _t.nemu_active = '__active'
    }, 400)
  },
  mounted() {
    this.fillData()
  },
  methods: {
    downloadCSV() {
      console.log(this.items)
      var csv = '\ufeff' + 'area,happiness,contract_rate,pareto_optimal_flag\n'
      this.items.forEach(el => {
        var line =
          el['area'] +
          ',' +
          el['happiness'] +
          ',' +
          el['contract_rate'] +
          ',' +
          el['pareto_optimal_flag'] +
          '\n'
        csv += line
      })
      let blob = new Blob([csv], { type: 'text/csv' })
      let link = document.createElement('a')
      link.href = window.URL.createObjectURL(blob)
      link.download = 'Result.csv'
      link.click()
    },
    next() {
      if (!(this.current_num == 10)) {
        //10番目の質問は数値なのでスキップ
        this.answer[this.current_num] =
          this.options[this.current_num].indexOf(
            this.answer[this.current_num]
          ) + 1
      }
      this.current_num += 1
      console.log(this.answer)
      if (this.current_num == 12) {
        let backend_url = API_BASE_URI + '/get_pareto'
        axios
          .post(backend_url, { answer: this.answer })
          .then(res => {
            console.log(res)
            // this.nemu_active = '__hide';
            // this.result_active = '__active';
            // const data = res.data;
            // console.log(data)
            // this.result = data
            // if (data[0]) {
            //   this.result1 = "第1位 " + data[0]['area']
            // }
            // if (data[1]) {
            //   this.result2 = "第2位 " +  data[1]['area']
            // }
            // if (data[2]) {
            //   this.result3 = "第3位 " + data[2]['area']
            // }
            // if (!data[0]) {
            //   this.result1 = "おすすめの地域はありません" //データがなかった場合
            // }
            const data = res.data
            console.log(data)
            const area = data['area']
            const contract_rate = data['contract_rate']
            const happiness = data['happiness']
            const pareto_optimal_flag = data['pareto_optimal_flag']
            console.log(area.length)
            console.log(happiness)
            console.log(contract_rate)
            let add_data = this.datacollection.datasets[0].data
            let add_data2 = this.datacollection.datasets[1].data
            for (let i = 0; i < area.length; i++) {
              this.items.push({
                area: area[i],
                happiness: happiness[i],
                contract_rate: contract_rate[i],
                pareto_optimal_flag: pareto_optimal_flag[i]
              })
              let newPoint = {
                x: happiness[i],
                y: contract_rate[i]
              }
              // this.$store.commit('mutateScatterPlot', newPoint);
              if (pareto_optimal_flag[i] == true) {
                add_data.push(newPoint)
              } else {
                add_data2.push(newPoint)
              }
            }
            this.datacollection = {
              labels: [this.getRandomInt()],
              datasets: [
                {
                  label: 'Data One',
                  backgroundColor: '#E53935',
                  data: add_data
                },
                {
                  label: 'Data Two',
                  backgroundColor: '#283593',
                  data: add_data2
                }
              ]
            }
            this.scatter_options = {
              legend: {
                display: false
              },
              scales: {
                xAxes: [
                  {
                    display: true,
                    scaleLabel: {
                      display: true,
                      labelString: '幸福度'
                    }
                  }
                ],
                yAxes: [
                  {
                    display: true,
                    scaleLabel: {
                      display: true,
                      labelString: '成約率'
                    }
                  }
                ]
              },
              tooltips: {
                callbacks: {
                  label: function(tooltipItem, data) {
                    var label = data.datasets[tooltipItem.datasetIndex].label
                    var d = data.datasets[tooltipItem.datasetIndex].data

                    var total = Number(0)
                    d.forEach(function(q) {
                      total = total + q
                    })
                    console.log(label)
                    var labelText = area[tooltipItem.index]
                    labelText +=
                      ' \n  幸福度：' +
                      String(happiness[tooltipItem.index]) +
                      ' \n 成約率：' +
                      String(contract_rate[tooltipItem.index])
                    return labelText
                  }
                }
              }
            }
            this.nemu_active = '__hide'
            this.result_active = '__active'
          })
      }
    },
    fillData() {
      this.datacollection = {
        labels: [this.getRandomInt()],
        datasets: [
          {
            backgroundColor: 'rgb(252, 209, 42,0)',
            data: []
          },
          {
            backgroundColor: 'rgb(17, 30, 108)',
            data: []
          }
          //  {
          //   label: 'Data One',
          //   backgroundColor: '#f87979',
          //   data: [{ x: this.getRandomInt(),  y:  this.getRandomInt()}, { x: this.getRandomInt(),  y: this.getRandomInt()}]
          // }
        ]
      }
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    },

    restart() {
      this.$router.push({
        name: 'home'
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
body {
  font-family: 'Hannari';
}

.Diagnosis {
  width: 100%;
  margin: 0 auto;
  overflow: hidden;
}
.result {
  width: 90%;
  margin: 0 auto;
  display: flex;
  text-align: center;
  font-weight: bold;
  display: none;
  &.__active {
    display: block;
  }
  &_inner {
    padding: 50px 0;
    font-size: 20px;
  }
  &_contents {
    width: 100%;
    border: 15px solid #ff6500;
    transition: all 1.5s;
    padding: 100px 20px;
    font-size: 50px;
    box-sizing: border-box;
  }
}
.menubox {
  overflow: hidden;
  justify-content: center;
  display: flex;
  padding: 80px 0;
  text-align: center;
  font-size: 30px;
  width: 100%;
  margin: 0 auto;
  opacity: 0;
  transition: all 0.4s ease 0.5s;
  &.__hide {
    display: none;
  }
  &.__active {
    opacity: 1;
  }
}
.menuttl {
  width: 100%;
  text-align: center;
  font-size: 1.8rem;
  vertical-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
.menuttl .txt {
  display: inline-block;
  vertical-align: center;
  font-size: 2.5rem;
  margin-left: 2rem;
}
.menuItem {
  min-width: 100%;
  transition: all 1.5s;
  padding: 10px 0;
  display: flex;
  justify-content: start;
  align-items: center;
  flex-wrap: wrap;
  label {
    padding: 10px;
    cursor: pointer;
    position: relative;
    display: inline-block;
    margin-right: 10px;

    input {
      display: none;
    }
    input + .btn {
      border: 1px solid #ccc;
      content: '';
      width: 100%;
      height: 100%;
      display: block;
      position: absolute;
      top: 0;
      left: 0;
      border-radius: 8px;
      transition: 0.8;
    }
  }
  input:checked + .btn {
    background: #ff6500;
    border: 1px solid #ff6500;
  }
  input:checked + .btn + .btn-txt {
    color: #fff;
  }
  .btn-txt {
    z-index: 10;
    position: relative;
  }
  .menuRadio {
    margin-top: 40px;
    min-width: 100%;
    max-width: 10px;
    padding: 10px;
    font-size: 20px;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s ease;
}
.fade-enter,
.fade-leave {
  opacity: 0;
}

h1 {
  margin: 40px 0 0;
  color: #409eff;
  font-family: 'PingFang SC';
  font-size: 200px;
}

.team {
  margin-top: 20px;
  margin-left: 20px;
  color: #409eff;
  font-family: 'PingFang SC';
}

.box {
  height: 50px;
}

.money-input {
  width: 100px;
}
</style>
