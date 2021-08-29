import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Random from './views/Random.vue'
import Diagnosis from './views/Diagnosis.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/random',
      name: 'random',
      component: Random
    },
    {
      path: '/diagnosis',
      name: 'diagnosis',
      component: Diagnosis
    },
  ]
})
