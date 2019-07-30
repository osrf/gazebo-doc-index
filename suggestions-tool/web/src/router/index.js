import Vue from 'vue'
import Router from 'vue-router'
import IssueTracker from '@/components/IssueTracker'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'IssueTracker',
      component: IssueTracker
    }
  ]
})
