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
  padding: 0 10px;
}
.head {
  height: 60px;
  border: 1px solid #9b9b9b;
  margin-bottom: 20px;
}
.aside {
  width: 100%;
  height: 100%;
  float: left;
  background-color: #545c64;
}
.main {
  float: left;
}
</style>
