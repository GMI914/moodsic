import axios from "axios";

export const ajax = axios.create({
    baseURL: 'http://0.0.0.0:8000/'
})

export const apiUrls = {
    musicList: '/api/music/music/',
    musicDetail: id => `/api/music/music/${id}/`,
    itemToUserMusicList: '/api/music/music/item_to_user/',
    itemToItemMusicList: '/api/music/music/item_to_item/',
};

