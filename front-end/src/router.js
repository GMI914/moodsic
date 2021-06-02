import DesignTest from './components/DesignTest.vue'
import Login from './components/pages/Login.vue'
import Questions from './components/pages/Questions.vue'
import Register from './components/pages/Register.vue'
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
