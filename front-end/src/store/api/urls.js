import axios from "axios";

export const ajax = axios.create({
    baseURL: 'http://127.0.0.1:8000/'
})

export const apiUrls = {
    musicList: '/api/music/music/',
    musicDetail: id => `/api/music/music/${id}/`,
    registerUser: '/api/user/register/',
    loginUser: '/api/user/getToken/'
};

