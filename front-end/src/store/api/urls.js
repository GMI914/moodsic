import axios from "axios";
import token from "../../utils/token"

export const ajax = axios.create({
    baseURL: 'http://127.0.0.1:8000/'
})

export const authAjax = () => {
    if (token.isAuthorized) {
        ajax.defaults.headers.common.Authorization = `Token ${token.userToken}`
    }
    return ajax
}


export const apiUrls = {
    musicList: '/api/music/music/',
    musicDetail: id => `/api/music/music/${id}/`,
    registerUser: '/api/user/register/',
    loginUser: '/api/user/getToken/',
    sendRating: '/api/music/music/send_rating/' 
};

