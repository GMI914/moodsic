<template>
    <div>
        <iframe v-if="playedMusic" id="ytplayer" type="text/html" width="640" height="360"
                :src="`https://www.youtube.com/embed/${playedMusic.video_id}?autoplay=1&origin=http://0.0.0.0:8080`"
                frameborder="0"></iframe>
        <h1 v-if="playedMusic">{{ playedMusic.title }}</h1>
        <h1 v-if="playedMusic">{{ playedMusic.views }}</h1>
        <ul>
            <li v-for="(music, index) in musicList" :key="index" @click="nextTrack(music)">{{
                    music.title
                }} | {{ music.views }}
            </li>
        </ul>
    </div>
</template>

<script>
import {ajax, apiUrls} from "../store/api/urls";

export default {
    name: 'HelloWorld',
    props: {
        msg: String
    },
    data() {
        return {
            musicList: [],
            playedMusic: null,
        }
    },
    methods: {
        nextTrack(music) {
            this.playedMusic = null
            setTimeout(() => {
                this.playedMusic = music
            }, 1)
            ajax.get(apiUrls.customMusicList, {params: {video_id: music.video_id}}).then(response => {
                this.musicList = response.data
            })
        }
    },
    mounted() {
        ajax.get(apiUrls.customMusicList).then(response => {
            this.musicList = response.data
            this.playedMusic = this.musicList.length ? this.musicList[0] : null
        })
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}
</style>
