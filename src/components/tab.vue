<template>
  <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
    <el-tab-pane label="近期数据" name="first">
      <Chartl></Chartl>
    </el-tab-pane>
    <el-tab-pane label="趋势预测" name="second">
      <Chartr></Chartr>
    </el-tab-pane>
    <el-tab-pane label="次日涨跌预测" name="third">
      hhh
    </el-tab-pane>
  </el-tabs>
</template>
<script>
import Chartl from "@/components/chartl.vue";
import Chartr from "@/components/chartr.vue";
export default {
  data() {
    return {
      activeName: '',
    };
  },
  components: {
    Chartl, 
    Chartr,
  },
  methods: {
    handleClick(tab, event) {
      this.activeName = tab.name;
      this.$bus.$emit('FocusEvent', tab.name);
      console.log(this.activeName);
    },
  },
};
</script>