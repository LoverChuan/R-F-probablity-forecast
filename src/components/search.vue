<template>
  <div class="search">
    <el-input v-model="input" placeholder="请输入日期区间长度"></el-input>
    <el-button type="primary" icon="el-icon-search" @click="handleClick()">显示</el-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: "",
    };
  },
  methods: {
    handleClick() {
      console.log('hi!', this.input);
      this.$bus.$emit('inputDateInterval', this.input);
    }
  }
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