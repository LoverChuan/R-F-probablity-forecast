<template>
  <div id="mainr" style="width: 1200px; height: 560px"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
  data() {
    return ({
      focusing: false,
      myChart: null,
      p0: [],
      p1: [],
      p2: [],
    })
  },
  watch: {
    p0() {
      this.$nextTick(() => {
        if (this.focusing) {
          this.chart();
        }
      })
    },
    focusing() {
      this.$nextTick(() => {
        if (this.focusing) {
          this.chart();
        }
      })
    },
  },
  mounted() {
    this.$bus.$on('FocusEvent', this.setfocus);
    this.$bus.$on('intervalDatar', this.demo);
    this.$bus.$on('shiftSideBar', this.reset);
    this.chart();
  },
  methods: {
    setfocus(name) {
      this.focusing = (name === 'second');
    },
    demo([d0, d1, d2]) {
      [this.p0, this.p1, this.p2] = [d0, d1, d2];
    },
    reset() {
      [this.p0, this.p1, this.p2] = [[], [], []];
    },
    chart() {
      this.myChart = echarts.init(document.getElementById("mainr"));
      var option = {
        title: {
          text: "预测对比图",
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: ["实际值", "预估值"],
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
        yAxis: {
          type: "value",
          min: "dataMin",
          max: "dataMax",
          axisLabel: {
            formatter: "{value} rmb"
          }
        },
        series: [
          {
            name: "实际值",
            type: "line",
            data: this.p1,
          },
          {
            name: "预估值",
            type: "line",
            data: this.p2,
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