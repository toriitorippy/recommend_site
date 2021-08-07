<template>
    <div id="Diagnosis" class="Diagnosis">
        <div class="menubox" v-bind:class="nemu_active">
            <transition-group name="fade" transition-mode="out-in">
                <div class="menuItem" key="1" v-if="current_num==0"><div class="menuttl">
                質問1<span class="txt">朝はパン？それともご飯？</span>
                </div>
                <div class="menuRadio"><label><input name="sex" type="radio" value="0" v-on:change="check" v-model="sex"><span class="btn"></span><span class="btn-txt">パン</span></label><label><input name="sex" type="radio" value="1" v-on:change="check" v-model="sex"><span class="btn"></span><span class="btn-txt">ごはん</span></label></div>
                </div>
                <div class="menuItem" key="2" v-if="current_num==1"><div class="menuttl">
                質問2<span class="txt">間食はしますか？</span>
                </div><div class="menuRadio"><label><input name="toilet" type="radio" value="0" v-on:change="check" v-model="toilet"><span class="btn"></span><span class="btn-txt">食べる</span></label><label><input name="toilet" type="radio" value="1" v-on:change="check" v-model="toilet"><span class="btn"></span><span class="btn-txt">食べない</span></label></div></div>
                <div class="menuItem" key="3" v-if="current_num==2"><div class="menuttl">
                質問3<span class="txt">昼食はどちらを食べたいですか？</span>
                </div>
                <div class="menuRadio"><label><input name="amount" type="radio" value="0" v-on:change="check" v-model="amount"><span class="btn"></span><span class="btn-txt">ハンバーグ</span></label><label><input name="amount" type="radio" value="1" v-on:change="check" v-model="amount"><span class="btn"></span><span class="btn-txt">グミ</span></label></div></div>
                <div class="menuItem" key="4" v-if="current_num==3"><div class="menuttl">
                質問4<span class="txt">晩ごはんは何が食べたいですか？</span>
                </div><div class="menuRadio"><label><input name="demand" type="radio" value="0" v-on:change="check" v-model="demand"><span class="btn"></span><span class="btn-txt">ステーキ</span></label><label><input name="demand" type="radio" value="1" v-on:change="check" v-model="demand"><span class="btn"></span><span class="btn-txt">カレーライス</span></label><label><input name="demand" type="radio" value="2" v-on:change="check" v-model="demand"><span class="btn"></span><span class="btn-txt">ナッツ</span></label></div>
                </div>
            </transition-group>
        </div>
        <div class="result" v-bind:class="result_active">
        <div class="result_inner">
            <transition-group name="fade">
            <div class="result_contents" key="1" v-if="result_num==1">
            診断結果 肉塊です
        </div>
        <div class="result_contents" key="2" v-if="result_num==2">
            診断結果 FATです
        </div>
        <div class="result_contents" key="3" v-if="result_num==3">
            診断結果 塊です
        </div>
        <div class="result_contents" key="4" v-if="result_num==4">
            診断結果 まあまあのポッチャリさんです
        </div>
        <div class="result_contents" key="5" v-if="result_num==5">
            診断結果 糖質改善ポッチャリです
        </div>
        <div class="result_contents" key="6" v-if="result_num==6">
            診断結果 甘党ぽっちゃりです
        </div>
        <div class="result_contents" key="7" v-if="result_num==7">
            診断結果 健康体です
        </div>
        <div class="result_contents" key="8" v-if="result_num==8">
            診断結果 大学生並
        </div>
        <div class="result_contents" key="9" v-if="result_num==9">
            診断結果 大学生並
        </div>
        <div class="result_contents" key="10" v-if="result_num==10">
            診断結果 普通です
        </div>
        <div class="result_contents" key="11" v-if="result_num==11">
            診断結果 普通です
        </div>
        <div class="result_contents" key="12" v-if="result_num==12">
            診断結果 小動物？
        </div>
        <div class="result_contents" key="13" v-if="result_num==13">
            診断結果 ポッチャリさんです
        </div>
        <div class="result_contents" key="14" v-if="result_num==14">
            診断結果 普通です
        </div>
        <div class="result_contents" key="15" v-if="result_num==15">
            診断結果 なぜ最後ナッツ入れた？
        </div>
        <div class="result_contents" key="16" v-if="result_num==16">
            診断結果 なぜグミいれた？
        </div>
        <div class="result_contents" key="17" v-if="result_num==17">
            診断結果 なぜグミいれた？
        </div>
        <div class="result_contents" key="18" v-if="result_num==18">
            診断結果 夜食べない派？
        </div>
        <div class="result_contents" key="19" v-if="result_num==19">
            診断結果 十分です
        </div>
        <div class="result_contents" key="20" v-if="result_num==20">
            診断結果 結構余裕ありますね
        </div>
        <div class="result_contents" key="21" v-if="result_num==21">
            診断結果 なぜ最後ナッツ？
        </div>
        <div class="result_contents" key="22" v-if="result_num==22">
            診断結果 けっこうええもん食うてる
        </div>
        <div class="result_contents" key="23" v-if="result_num==23">
            診断結果 大丈夫です
        </div>
        <div class="result_contents" key="24" v-if="result_num==24">
            診断結果 バイトしよか
        </div>
            </transition-group>
        </div>
        </div>
        <div class="detail">
            {{result_txt}}
        </div>
    </div>
</template>

<script>
var queData = [
  ['パン','ごはん'],
  ['食べる','食べない'],
  ['ハンバーグ','グミ'],
  ['ステーキ','カレーライス','ナッツ']
]


export default {
  name: 'Diagnosis',
  props: {
    msg: String
  },
  data() {
    return {
        answer:[],
        sex:'',
        current_num:0,
        toilet:'',
        amount:'',
        demand:'',
        result_active:'',
        nemu_active:'',
        result_txt:'',
        result:{
        '0000':1,
        '0001':2,
        '0002':3,
        '0010':4,
        '0011':5,
        '0012':6,
        '0100':7,
        '0101':8,
        '0102':9,
        '0110':10,
        '0111':11,
        '0112':12,
        '1000':13,
        '1001':14,
        '1002':15,
        '1010':16,
        '1011':17,
        '1012':18,
        '1100':19,
        '1101':20,
        '1102':21,
        '1110':22,
        '1111':23,
        '1112':24
        },
        result_num:'',
    };
  },
  watch: {
      result_num:function(n,o){
          print(n,o)
        this.result_txt = queData[0][this.sex]+' >> ' + queData[1][this.toilet] +' >> ' +queData[2][this.amount] +' >> ' +queData[3][this.demand] + ' を選択した時のコンテンツ'
      }
  },
  created:function(){
    var _t = this;
    setTimeout(function(){
      _t.nemu_active = '__active';
                         },400);
  },
  methods:{
    check:function(){
      this.answer[0] = this.sex;
      this.answer[1] = this.toilet;
      this.answer[2] = this.amount;
      this.answer[3] = this.demand;
      this.current_num = this.answer.indexOf('');
      
      if(this.answer.indexOf('')==-1){
        this.nemu_active = '__hide';
        this.result_active = '__active';
        this.result_num = this.result[this.answer.join('')];
      }
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
</style>
