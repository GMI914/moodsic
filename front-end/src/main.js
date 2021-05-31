import { createApp } from 'vue'
import App from './App.vue'

import YoutubeIframe from '@techassi/vue-youtube-iframe'
const app = createApp(App)

app.use(YoutubeIframe)
app.mount('#app')
