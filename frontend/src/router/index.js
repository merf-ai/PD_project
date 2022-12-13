import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/views/Main.vue'
import Info from '@/views/Info.vue'
import Account from '@/views/Account.vue'
import LogIn from '@/views/LogIn.vue'
import Register from '@/views/Register.vue'
import VerifyEmail from '@/views/VerifyEmail.vue'
import store from "@/store"

const routes = [
  {
    path: '/',
    name: 'home',
    component: Main
  },
  {
    path: '/info',
    name: 'info',
    component: Info
  },
  {
    path: '/account',
    name: 'account',
    component: Account
  },
  {
    path: '/login',
    name: 'login',
    component: LogIn
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/verifyemail/:uid/:token',
    name: 'verifyemail',
    component: VerifyEmail
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
