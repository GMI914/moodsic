import HomePage from './pages/HomePage.vue'
import Authentication from './pages/Authentication.vue'

export const routes = [
    {
        name: 'home',
        path: '/', component: HomePage
    },
    {
        name: 'login',
        path: '/login', component: Authentication
    },
]
