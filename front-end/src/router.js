import DesignTest from './components/DesignTest.vue'
import Login from './components/pages/Login.vue'
export const routes = [
    {
        name: 'home',
        path: '/', component: DesignTest
    },
    {
        name: 'login',
        path: '/login', component: Login
    },

]
