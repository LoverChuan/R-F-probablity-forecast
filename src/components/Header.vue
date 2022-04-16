<template>
  <div class="header">
    <div>
      <p>期货预测</p>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.header ::after {
  content: "";
  display: block;
  height: 0;
  clear: both;
  visibility: hidden;
}
.header > div:first-child {
  border: 1px solid #9b9b9b;
  background: rgb(43, 43, 43);
  width: 230px;
  float: left;
  margin: -1px 0 0 -1px;
}
p {
  text-align: center;
  color: #fff;
  font-size: 20px;
  font-weight: 500;
  line-height: 58px;
}
</style>