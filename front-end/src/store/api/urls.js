import axios from "axios";

export const ajax = axios.create({
    baseURL: 'http://0.0.0.0:8000/'
})

export const apiUrls = {
    musicList: '/api/music/music/',
    musicDetail: id => `/api/music/music/${id}/`,
    customMusicList: '/api/music/music/custom_list/',
};
