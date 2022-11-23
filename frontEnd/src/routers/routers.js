import { createWebHistory, createRouter } from "vue-router"

import SignUp from "@/views/auth/SignUp.vue"
import LogIn from "@/views/auth/LogIn.vue"
import ConfirmEmail from "@/views/auth/ConfirmEmail.vue"
import ConfirmEmailDone from "@/views/auth/ConfirmEmailDone.vue"
import PasswordRecover from '@/views/auth/PasswordRecover.vue'
import PasswordChange from '@/views/auth/PasswordChange.vue'

import HomeApp from "@/views/HomeApp.vue"

import authStore from "@/stores/modules/auth.store"

const routes = [
  {
    path: "/signup/",
    name: "SignUp",
    component: SignUp,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path: "/",
    name: "LogIn",
    component: LogIn,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path: "/confirm/email/:email/",
    name: "ConfirmEmail",
    component: ConfirmEmail,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path: "/confirm/email/:uidb64/:token/",
    name: "ConfirmEmailDone",
    component: ConfirmEmailDone,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path: "/recover/",
    name: "PasswordRecover",
    component: PasswordRecover,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path: "/password/change/:uidb64/:token/",
    name: "PasswordChange",
    component: PasswordChange,
    meta: {
      requiresAuth: false,
    }
  },
  {
    path: "/home/",
    name: "HomeApp",
    component: HomeApp,
    meta: {
      requiresAuth: true,
    }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {

  const requiresAuth = to.matched.some(record  => record.meta.requiresAuth)
  const isActive = authStore.state.accessToken

  if (requiresAuth && !isActive) {
      next('/')
  } else if (requiresAuth && isActive) {
      next()
  } else {
      next()
  }

})

export default router;