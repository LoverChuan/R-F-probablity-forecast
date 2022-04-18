<template>
  <el-tabs v-model="activeName" type="card" @tab-click="handleClick">
    <el-tab-pane label="近期数据统计" name="first">
      <Chart></Chart>
    </el-tab-pane>
    <el-tab-pane label="预测" name="second">预测</el-tab-pane>
  </el-tabs>
</template>
<script>
import Chart from "@/components/chart.vue";
export default {
  data() {
    return {
      activeName: "first",
    };
  },
  components: {
    Chart,
  },
  methods: {
    handleClick(tab, event) {
      console.log(tab, event);
    },
  },
};
</script>