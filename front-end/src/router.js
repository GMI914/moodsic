import DesignTest from './pages/DesignTest.vue'
import Questions from './pages/Questions.vue'

export const routes = [
    {
        name: 'question',
        path: '/questions', component: Questions
    },
    {
        name: 'home',
        path: '/', component: DesignTest
    },
  
]
