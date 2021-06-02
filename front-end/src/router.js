import DesignTest from './pages/DesignTest.vue'
import Login from './pages/Login.vue'
import Questions from './pages/Questions.vue'
import Register from './pages/Register.vue'

export const routes = [
    {
        name: 'question',
        path: '/', component: Questions
    },
    {
        name: 'home',
        path: '/home', component: DesignTest
    },
    {
        name: 'login',
        path: '/login', component: Login
    },
    {
        name: 'register',
        path: '/register', component: Register
    },
]
