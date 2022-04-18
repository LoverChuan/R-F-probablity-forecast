import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI);
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
	beforeCreate() {
		Vue.prototype.$bus = this
		//安装全局事件总线，$bus就是当前应用的vm
	},
}).$mount('#app')
