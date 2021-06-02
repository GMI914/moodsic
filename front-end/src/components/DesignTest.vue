<template>
    <div class="MainContainer">

        <div class="LeftRecommendation">

            <div class="playlist-items">

                <div class="playlist-item" v-for="(music,index) in ItemToUserList" :key="index">
                    <a @click="NextTrack(music)">
                        <div class="thumbnail-meta-container">
                            <div class="thumbnail-container">
                                <img :src="music.image_url"/>
                            </div>
                            <div class="meta">
                                <h4 class="title-style">
                                <span class="video-title">
                                    {{ music.title }}
                                </span>
                                </h4>
                            </div>
                        </div>
                    </a>
                </div>

            </div>

        </div>

        <div class="center">

            <div class="music-player">
                <div class="frame-wrapper">

                    <youtube-iframe
                        :player-width="playerSize / 3"
                        :player-height="playerSize * 3 / 16"
                        v-if="CurrentMusic && enablePlayer"
                        :video-id="CurrentMusic.video_id" @state-change="PlayerStateChange"
                        @ready="PlayerStateChange()"
                    ></youtube-iframe>
                </div>
                <div class="actions-wrapper">
                    <div class="action-item">
                        <svg width="25" height="25"></svg>
                    </div>
                    <div class="action-item">
                        <svg width="18" height="16"></svg>
                    </div>
                    <div class="action-item">
                        <svg width="18" height="16"></svg>
                    </div>
                    <div class="action-item">
                        <svg width="18" height="16"></svg>
                    </div>
                </div>
            </div>
        </div>


        <div class="right-recommend">
            <div class="playlist-items">

                <div class="playlist-item" v-for="(music,index) in ItemToItemList" :key="index">
                    <a @click="NextTrack(music)">
                        <div class="thumbnail-meta-container">
                            <div class="thumbnail-container">
                                <img :src="music.image_url"/>
                            </div>
                            <div class="meta">
                                <h4 class="title-style">
                                <span class="video-title">
                                    {{ music.title }}
                                </span>
                                </h4>
                            </div>
                        </div>
                    </a>
                </div>

            </div>
        </div>

    </div>
</template>

<script>
import {ajax, apiUrls} from "../store/api/urls";

export default {
    name: 'DesignTest',
    props: {msg: String},
    data() {
        //Why does the return force me to put the { on the same line?????
        return {
            ItemToUserList: [],
            ItemToItemList: [],
            CurrentMusic: null,
            screenWidth: 0,
            enablePlayer: true,
        }
    },
    methods: {
        NextTrack(music) {
            this.CurrentMusic = null
            setTimeout(() => {
                this.CurrentMusic = music
            }, 1)
        },
        PlayerStateChange(event) {
            console.log(event)
        },
        resizeEvent() {
            this.enablePlayer = false
            setTimeout(() => {
                this.enablePlayer = true
            }, 1)
            this.screenWidth = window.innerWidth
        }
    },
    computed: {
        playerSize() {
            return this.screenWidth ? this.screenWidth : 0
        },
    },
    mounted() {
        this.screenWidth = window.innerWidth
        window.addEventListener('resize', this.resizeEvent)
        ajax.get(apiUrls.itemToUserMusicList).then(response => {
            this.ItemToUserList = response.data
            this.CurrentMusic = this.ItemToUserList.length ? this.ItemToUserList[0] : null
            if (this.CurrentMusic) {
                ajax.get(apiUrls.itemToItemMusicList, {params: {video_id: this.CurrentMusic.video_id}}).then(response => {
                    this.ItemToItemList = response.data
                })
            }
        })
    },
    unmounted() {
        window.removeEventListener('resize', this.resizeEvent)
    }
}

</script>


<style scoped>
/*
TODO LIST:
Add breakpoints

Turn dimensions into ratios
*/


a {
    cursor: pointer;
    display: block;
    flex-basis: 1 e-09px;

    /*these two are playing a huge role*/
    flex-grow: 1;
    flex-shrink: 1;

    min-width: 0px;
    text-decoration-color: rgb(3, 3, 3);
    text-size-adjust: 100%;
}

a:hover {
    background-color: #254f64;
    size: 20px;
    border-radius: 3px;
    cursor: pointer;

}

.MainContainer {

    display: grid;
    grid-template-areas:
    'left main right';
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 10px;
    padding-left: 15px;
    padding-right: 15px;

    background-color: #1a1a1d;

    border-radius: 15px;
    border-left: 5px solid #ff2556;
    border-right: 5px solid #ff2556;
    opacity: 0.91;
}

.MainContainer > div {
    text-align: center;
    padding: 20px 0;
    font-size: 30px;
}

.center {
    background-color: #262626;

    grid-area: main;

    margin-top: 12px;
    border-radius: 20px;
    border-top: 6px solid #c3073f;
    border-bottom: 6px solid #c3073f;
    color: #4e4e50;
    box-shadow: 5px 5px 10px 5px rgba(9, 32, 71, 0.6);

}

.music-player {
    display: flex;
    flex-direction: column;
}


svg {
    background-color: #c3073f;
    width: 35px;
    height: 35px;
    border-radius: 20px;
    cursor: pointer;
}

.actions-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.action-item {
    margin: 5px;
    align-items: center;
}

.LeftRecommendation {
    background-color: #262626;

    grid-area: left;

    display: flex;
    flex-direction: column;
    font-size: 10px;
    max-height: 460px;
    margin-top: 24px;
    margin-bottom: 24px;

    border-radius: 20px;
    border-top: 6px solid #c3073f;
    border-bottom: 6px solid #c3073f;
    color: #4e4e50;
    box-shadow: 5px 5px 10px 5px rgba(9, 32, 71, 0.6);


}

.playlist-items::-webkit-scrollbar {
    width: 5px;
}

.playlist-items::-webkit-scrollbar-thumb {
    background-color: #c3073f;
}

.playlist-items::-webkit-scrollbar-track {
    background-color: #262626;
}

.right-recommend {
    background-color: #262626;

    grid-area: right;

    display: flex;
    flex-direction: column;
    font-size: 10px;
    max-height: 460px;
    margin-top: 24px;
    margin-bottom: 24px;

    border-radius: 20px;
    border-top: 6px solid #c3073f;
    border-bottom: 6px solid #c3073f;
    color: #4e4e50;
    box-shadow: 5px 5px 10px 5px rgba(9, 32, 71, 0.6);

}

.playlist-items {

    overflow-y: auto;
    margin: 0 0 0 0;
    height: 363px;
    font-size: 10px;
    display: block;
    text-size-adjust: 100%;
}

.playlist-item {
    display: flex;
    flex-direction: row;
    font-size: 10px;
    height: 56px;
    padding: 4px 8px 0px 4px;
}

.thumbnail-meta-container {
    /*These two also play a part*/
    display: flex;
    flex-direction: row;

    margin: 0 0 0 0;
    padding: 0 0 0 0;
}

.thumbnail-container {
    display: block;
    overflow-x: hidden;
    overflow-y: hidden;
    text-align: center;

    width: 100px;
    height: 56px;
    flex-basis: auto;
    flex-grow: 0;
    flex-shrink: 0;
}

.thumbnail-container img {
    height: 100%;

    /*
    These need further work
    transform: translateY(-50%);
    top: 50%;
    left: 0;
    */
}

.meta {
    min-width: 0;
    padding: 0 8px;
    display: flex;
    flex-direction: column;
    /*Let all the flexible items be the same length, regardless of its content:*/
    flex: 1;
}

.title-style {
    display: block;
    cursor: pointer;
    margin: 0 0 0 0;
    padding: 0 0 0 0;
    text-size-adjust: 100%;
    font-weight: bold;

    /*
    Don't understand these
    margin-block-start: 1.33em;
    margin-block-end: 1.33em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    */
}

.video-title {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    overflow: hidden;

    /*
    this puts dots(...) after the text if it overflows
    but it doesn't work without the previous stuff
    */
    text-overflow: ellipsis;


    margin: 0 0 4px 0;
    padding: 0;


    font-size: 14px;
    font-weight: 500;
    text-decoration-thickness: initial;
    white-space: normal;
}

</style>