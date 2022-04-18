import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    {
      path: '/',
      component: Home,
      meta: { title: "主页" }
    },
  ]
})

router.afterEach((to, from) => { //后置路由守卫实现标题切换 
  document.title = to.meta.title
})

export default router