<template>
<!--参考サイト：http://work2work.work/diagnosis/-->
    <div id="Diagnosis" class="Diagnosis">
    <h2 class="team text-left">KOKOSUMU</h2>
        <div class="menubox" v-bind:class="nemu_active">
            <div>
                <div class="menuItem" key="1" v-if="current_num==0">
                <el-card class="box-card">
                    <div class="menuttl">
                      <span class="txt">Q1.通勤や通学に便利であることが大切だ</span>
                    </div>
                    <div class="menuRadio">
                      <label>
                        <el-button plain v-on:click="check(0,0)">はい</el-button>
                      </label>
                      <label>
                        <el-button plain v-on:click="check(0,1)">いいえ</el-button>
                      </label>
                    </div>
                    <img class="img" src="../assets/images/undraw_Site_stats_re_ejgy.png" style="width: 50%"  />
                </el-card>
                </div>

                <div class="menuItem" key="2" v-if="current_num==1">
                  <el-card class="box-card">
                    <div class="menuttl">
                      <span class="txt">Q2.活気あふれる都市部で暮らしたい？</span>
                    </div>
                    <div class="menuRadio">
                      <label>
                        <el-button plain v-on:click="check(1,0)">はい</el-button>
                      </label>
                      <label>
                        <el-button plain v-on:click="check(1,1)">いいえ</el-button>
                      </label>
                    </div>
                    <img class="img" src="../assets/images/undraw_Partying_re_at7f.png" style="width: 40%"  />
                  </el-card>
                </div>

                <div class="menuItem" key="3" v-if="current_num==2">
                  <el-card class="box-card">
                    <div class="menuttl">
                      <span class="txt">Q3.家族と過ごす時間をなるべく多くしたい？</span>
                    </div>
                    <div class="menuRadio">
                        <label>
                          <el-button plain v-on:click="check(2,0)">はい</el-button>
                        </label>
                        <label>
                          <el-button plain v-on:click="check(2,1)">いいえ</el-button>
                        </label>
                    </div>
                    <img class="img" src="../assets/images/undraw_Chilling_re_4iq9.png" style="width: 50%"  />
                  </el-card>
                </div>

                <div class="menuItem" key="4" v-if="current_num==3">
                  <el-card class="box-card">
                    <div class="menuttl">
                      <span class="txt">Q4.生まれ育った地に住み続けたい？</span>
                    </div>
                    <div class="menuRadio">
                        <label>
                          <el-button plain v-on:click="check(3,0)">はい</el-button>
                        </label>
                        <label>
                          <el-button plain v-on:click="check(3,1)">いいえ</el-button>
                        </label>
                        <label>
                          <el-button plain v-on:click="check(3,2)">どちらでもいい</el-button>
                        </label>
                    </div>
                    <img class="img" src="../assets/images/undraw_web_shopping_re_owap.png" style="width: 50%"  />
                  </el-card>
                </div>
            </div>
        </div>

        <div class="result" v-bind:class="result_active">
          <div class="box"></div>
            <div class="menuttl">
              <span class="txt">あなたの住みやすい街は...</span>
            </div>
            <h1>中央区</h1>
            <img class="img" src="../assets/images/undraw_Ordinary_day_re_v5hy.png" style="width: 40%"  />
            <div class="box"></div>
            <el-button plain type="primary" round v-on:click="restart()">戻る</el-button>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Diagnosis',
  props: {
    msg: String
  },
  data() {
    return {
        answer:[],
        current_num:0,
        nemu_active: '',
    };
  },
  watch: {
      result_num:function(n,o){
        print(n,o)
      }
  },
  created:function(){
    var _t = this;
    setTimeout(function(){
      _t.nemu_active = '__active';
                         },400);
  },
  methods:{
    check (id,value) {
      console.log(value)
      this.answer[id] = value;
      this.current_num = id + 1;
      console.log(this.answer)
      if(this.current_num==4){
        this.nemu_active = '__hide';
        this.result_active = '__active';
        this.result_num = this.result[this.answer.join('')];
      }
    },
    restart () {
      this.$router.push({
        name: 'home',
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
body{
  font-family:'Hannari';
}

.Diagnosis{
 width:100%;
  margin:0 auto;
  overflow:hidden;
}
.result{
  width:90%;
  margin:0 auto;
  display:flex;
  text-align:center;
  font-weight:bold;
  display:none;
  &.__active{
    display:block;
  }
  &_inner{
    padding:50px 0;
    font-size:20px;
  }
  &_contents{
    width:100%;
    border:15px solid #ff6500;
    transition: all 1.5s;
    padding:100px 20px;
    font-size:50px;
    box-sizing:border-box;
  }
}
.menubox{
  overflow:hidden;
  justify-content:center;
  display:flex;
  padding:80px 0;
  text-align:center;
  font-size:30px;
  width:100%;
  margin:0 auto;
  opacity:0;
  transition:all .4s ease .5s;
  &.__hide{
    display:none;
  }
  &.__active{
    opacity:1;
  }
}
.menuttl{
  width:100%;
  text-align:center;
  font-size:1.8rem;
  vertical-align:center;
  display:flex;
  justify-content:center;
  align-items:center;
}
.menuttl .txt{
  display:inline-block;
  vertical-align:center;
  font-size:2.5rem;
  margin-left: 2rem;
}
.menuItem{
  min-width:100%;
  transition: all 1.5s;
  padding:10px 0;
  display:flex;
  justify-content:start;
  align-items:center;
  flex-wrap:wrap;
  label{
    padding:10px;
    cursor:pointer;
    position:relative;
    display:inline-block;
    margin-right: 10px;
    
    
    input{
      display:none;
    }
    input + .btn{
        border:1px solid #CCC;
        content:"";
        width:100%;
        height:100%;
      display:block;
      position:absolute;
      top:0;
      left:0;
      border-radius:8px;
      transition:.8;
     }
  }
  input:checked + .btn{
    background:#ff6500;
    border:1px solid #ff6500;
  }
  input:checked + .btn + .btn-txt{
    color:#FFF;
  }
  .btn-txt{
    z-index:10;
    position:relative;
  }
  .menuRadio{
    margin-top: 40px;
    min-width:100%;
   padding:10px;
    font-size:20px;
  }
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 1s ease;
}
.fade-enter, .fade-leave {
  opacity: 0
}

h1 {
  margin: 40px 0 0;
  color: #409EFF;
  font-family: "PingFang SC";
  font-size: 200px;
}

.team{
  margin-top: 20px;
  margin-left:20px;
  color: #409EFF;
  font-family: "PingFang SC";
}

.box {
  height:50px;
}

</style>
