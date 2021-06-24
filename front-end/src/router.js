import HomePage from './pages/HomePage.vue'
import Questions from './pages/Questions.vue'
import Authentication from './pages/Authentication.vue'

export const routes = [
    {
        name: 'question',
        path: '/questions', component: Questions
    },
    {
        name: 'home',
        path: '/', component: HomePage
    },
    {
        name: 'login',
        path: '/login', component: Authentication
    },
]
