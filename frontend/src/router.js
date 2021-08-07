import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from './views/HelloWorld.vue'
import Random from './views/Random.vue'
import Example from './views/Example.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: HelloWorld
    },
    {
      path: '/random',
      name: 'random',
      component: Random
    },
    {
      path: '/example',
      name: 'example',
      component: Example
    },
  ]
})
