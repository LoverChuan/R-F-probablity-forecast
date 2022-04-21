<template>
  <div>
    <el-container>
      <el-header>
        <div class="head">
          <Header></Header>
        </div>
      </el-header>
      <el-container>
        <el-aside width="220px">
          <div class="aside">
            <Aside> </Aside>
          </div>
        </el-aside>
        <el-main>
          <div class="main">
            <Main></Main>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Aside from "@/components/aside.vue";
import Main from "@/components/main.vue";

export default {
  components: {
    Header,
    Aside,
    Main,
  },
  data() {
    return ({
      category: 'ag',
      interval: 0,
      focusing: '',
    });
  },
  mounted() {
    this.$bus.$on('inputDateInterval', this.restoreData);
    this.$bus.$on('shiftSideBar', this.chooseCategory);
    this.$bus.$on('FocusEvent', this.setFocus);
  },
  methods: {
    readFile(filePath) {
      return new Promise(function (resolve, reject) {
        let xhr = new XMLHttpRequest();
        xhr.open("get", filePath, true);
        xhr.responseType = "blob";
        xhr.onload = function() {
          if (this.status == 200) {
            const reader = new FileReader();
            reader.onload = function() {
              resolve(reader.result);
            }
            reader.readAsText(this.response);
          } else {
            console.log('err');
          }
        }
        xhr.send();
      })
    },
    setFocus(name) {
      this.focusing = name;
    },
    restoreData(length) {
      console.log("category:", this.category);
      this.interval = length;
      let d0 = [], d1 = [], d2 = [], d3 = [], d4 = [], d5 = [], d6 = [], d7 = [], arr, temparr;
      this.readFile(`0_${this.category}_15m.txt`).then(res0 => {
        arr = res0.split('\r\n'), temparr;
        for (let i = length - 1; i >= 0; --i) {
          temparr = JSON.parse(arr[i]);
          d0.push(temparr[0]);
          d1.push(temparr[1]);
          d2.push(temparr[2]);
          d3.push(temparr[3]);
          d4.push(temparr[4]);
          d5.push(temparr[5]);
          d6.push((temparr[1] + temparr[2]) / 2);
        }
        
        console.log("focusing:", this.focusing);

        this.readFile(`1_${this.category}_15m.txt`).then(res1 => {
          arr = res1.split('\r\n')
          for (let i = length - 1; i >= 0; --i) {
            temparr = JSON.parse(arr[i]);
            d7.push(temparr[1]);
          }
        }).then(() => {
          console.log(d7);
          if (this.focusing === 'first') {
            this.$bus.$emit('intervalDatal', [d0, d1, d2, d3, d4, d5]);
            return;
          } else
          if (this.focusing === 'second') {
            this.$bus.$emit('intervalDatar', [d0, d6, d7]);
            return;
          }
        });
      })
    },
    chooseCategory(ca) {
      this.category = ca;
    },
  },

};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.el-container .el-header {
  padding: 0;
}
.el-aside {
  padding: 0px 0px 0px 0px;
}
.head {
  height: 60px;
  border: 1px solid #9b9b9b;
  margin-bottom: 20px;
}
.aside {
  height: 100%;
  float: left;
  background-color: #545c64;
}
.main {
  float: left;
}
</style>
