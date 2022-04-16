<template>
  <div class="search">
    <el-input v-model="input" placeholder="请输入商品名称"></el-input>
    <el-button type="primary" icon="el-icon-search">搜索</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: "",
    };
  },
};
</script>
<style scoped>
.search {
  height: 60px;
  line-height: 60px;
}
.search > span {
  font-weight: 700;
  font-size: 20px;
  float: left;
  margin: 0 10px;
}
.search ::after {
  content: "";
  display: block;
  height: 0;
  clear: both;
  visibility: hidden;
}
.el-input {
  float: left;
  width: 200px;
  margin: 0 10px;
}
.el-button {
  margin: 0 10px;
}
</style>