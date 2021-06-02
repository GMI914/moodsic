import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import { routes } from './router.js'

import App from './App.vue'


import YoutubeIframe from '@techassi/vue-youtube-iframe'

const router = createRouter({
    history: createWebHistory(),
    routes
})

const app = createApp(App)

app.use(router);

app.use(YoutubeIframe)
app.mount('#app')
