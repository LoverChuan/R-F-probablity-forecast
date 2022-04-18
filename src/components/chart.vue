<template>
  <div id="main" style="width: 1200px; height: 560px"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
  data() {
    return ({
      myChart: null,
      p0: [],
      p1: [],
      p2: [],
      p3: [],
      p4: [],
      p5: [],
    })
  },
  watch: {
    p0() {
      this.$nextTick(() => {
        this.chart();
      })
    },
  },
  mounted() {
    this.$bus.$on('intervalData', this.demo);
    this.$bus.$on('shiftSideBar', this.reset);
    this.chart();
  },
  methods: {
    demo([d0, d1, d2, d3, d4, d5]) {
      [this.p0, this.p1, this.p2, this.p3, this.p4, this.p5] = [d0, d1, d2, d3, d4, d5];
    },
    reset() {
      [this.p0, this.p1, this.p2, this.p3, this.p4, this.p5] = [[], [], [], [], [], []];
    },
    chart() {
      this.myChart = echarts.init(document.getElementById("main"));
      var option = {
        title: {
          text: "趋势折线图",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["开盘价", "收盘价", "最高价", "最低价", "交易量"],
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        toolbox: {
          feature: {
            saveAsImage: {},
          },
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: this.p0,
        },
        yAxis: [{
          type: "value",
          min: "dataMin",
          max: "dataMax",
          position: "left",
          axisLabel: {
            formatter: "{value} rmb"
          }
        },
        {
          type: "value",
          min: "dataMin",
          max: "dataMax",
          position: "right",
          axisLabel: {
            formatter: "{value} 单"
          }
        }],
        series: [
          {
            name: "开盘价",
            type: "line",
            yAxisIndex: 0,
            data: this.p1,
          },
          {
            name: "收盘价",
            type: "line",
            yAxisIndex: 0,
            data: this.p2,
          },
          {
            name: "最高价",
            type: "line",
            yAxisIndex: 0,
            data: this.p3,
          },
          {
            name: "最低价",
            type: "line",
            yAxisIndex: 0,
            data: this.p4,
          },
          {
            name: "交易量",
            type: "line",
            yAxisIndex: 1,
            data: this.p5,
          },
        ],
      };

      option && this.myChart.setOption(option);
    },
  },
};
</script>

<style>
</style>