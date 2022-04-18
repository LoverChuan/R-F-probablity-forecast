<template>
  <!-- 侧边可以做商品的分类-->
  <div class="aside-container">
    <el-col>
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        collapse=true
      >
        <el-menu-item index="1">
          <i class="el-icon-document"></i>
          <span slot="title">介绍</span>
        </el-menu-item>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span>商品类型</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="ag" @click=handleClick>ag</el-menu-item>
            <el-menu-item index="al" @click=handleClick>al</el-menu-item>
            <el-menu-item index="au" @click=handleClick>au</el-menu-item>
            <el-menu-item index="bu" @click=handleClick>bu</el-menu-item>
            <el-menu-item index="cf" @click=handleClick>cf</el-menu-item>
            <el-menu-item index="cu" @click=handleClick>cu</el-menu-item>
            <el-menu-item index="dci" @click=handleClick>dci</el-menu-item>
            <el-menu-item index="dcp" @click=handleClick>dcp</el-menu-item>
            <el-menu-item index="fg" @click=handleClick>fg</el-menu-item>
            <el-menu-item index="j" @click=handleClick>j</el-menu-item>
            <el-menu-item index="jm" @click=handleClick>jm</el-menu-item>
            <el-menu-item index="ma" @click=handleClick>ma</el-menu-item>
            <el-menu-item index="ni" @click=handleClick>ni</el-menu-item>
            <el-menu-item index="pb" @click=handleClick>pb</el-menu-item>
            <el-menu-item index="rb" @click=handleClick>rb</el-menu-item>
            <el-menu-item index="sn" @click=handleClick>sn</el-menu-item>
            <el-menu-item index="sr" @click=handleClick>sr</el-menu-item>
            <el-menu-item index="zn" @click=handleClick>zn</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-col>
  </div>
</template>

<script>
export default {
  methods: {
    handleClick(event) {
      this.$bus.$emit('shiftSideBar', event.index);
    }
  },
};
</script>

<style scoped>
</style>