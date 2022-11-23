import { createApp } from 'vue'
import App from './App.vue'
import '@/assets/css/main.css'

import router from '@/routers/routers'
import store from '@/stores'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"


/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from "@fortawesome/fontawesome-svg-core"
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'

import jwtInterceptor from '@/shared/jwt.interceptor'

library.add(fas, fab, far)

const app = createApp(App)

app.use(store)
app.use(router)

app.config.globalProperties.$axios = {...jwtInterceptor}

app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')