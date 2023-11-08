// Composables
import { createRouter, createWebHistory } from 'vue-router'
import Prompt from '../components/Prompt.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Prompt
    },
  ]
})

export default router
