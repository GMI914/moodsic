<template>
    <div class="MainContainer">
        <div class="left-recommended">
            <div class="ghost">
                <Ghost></Ghost>
            </div>
            <div class="question-box">
                <p>
                    Hi {{ user.username || 'Buddy' }} <br/>
                    How do you feel today?
                </p>
                <ul>
                    <label>
                        <li>
                            <input id="happy" name="mood" type="radio" value="happy" v-model="moodValue"/>
                            <i> Happy</i>
                        </li>
                    </label>
                    <label>
                        <li>
                            <input id="cheerful" name="mood" type="radio" value="cheerful" v-model="moodValue"/>
                            <i> Cheerful</i>
                        </li>
                    </label>
                    <label>
                        <li>
                            <input id="gloomy" name="mood" type="radio" value="gloomy" v-model="moodValue"/>
                            <i> Gloomy</i>
                        </li>
                    </label>
                    <label>
                        <li><input id="sad" name="mood" type="radio" value="sad" v-model="moodValue"/>
                            <i> Sad</i></li>
                    </label>
                </ul>
            </div>
            <div class="wrapper" @click="filterByMood">
                <span>Filter !</span>
            </div>
        </div>

        <div class="center">
            <div class="music-player">
                <div class="frame-wrapper">
                    <youtube-iframe
                        ref="player"
                        :noCookie="true"
                        :playerParameters="playerParameters"
                        :player-width="playerSize / 3"
                        :player-height="(playerSize * 3) / 16"
                        v-if="CurrentMusic && enablePlayer"
                        :video-id="CurrentMusic.video_id"
                        @state-change="PlayerStateChange"
                        @ready="playerReady"
                    ></youtube-iframe>
                </div>
                <div class="actions-wrapper">
                    <div class="action-item" @click="SendRating('like'); AnimateButton($event)">
                        <img src="../assets/like.svg"/>
                    </div>
                    <div class="action-item" @click="SendRating('dislike'); AnimateButton($event)">
                        <img src="../assets/dislike.svg"/>
                    </div>
                    <div class="action-item" @click="AddToPlaylist(); AnimateButton($event);"
                         :class="{'active': isFavorite(CurrentMusic)}">
                        <img src="../assets/heart.svg"/>
                    </div>
                    <div class="action-item" @click="Share">
                        <img src="../assets/share.svg"/>
                    </div>
                </div>
            </div>
        </div>
        <div class="right-recommended">
            <div class="tabs">
                <div
                    class="tab-recomended"
                    @click="ChangeTab('recomended')"
                    :class="{ active: IsTabActive }"
                >
                    Recommended
                </div>
                <div
                    class="tab-favorite"
                    @click="ChangeTab('favorite')"
                    :class="{ active: !IsTabActive }"
                >
                    Favorites
                </div>
            </div>
            <div class="playlist-items">
                <template v-if="IsTabActive">
                    <template v-for="(music, index) in ItemToUserList">
                        <div class="playlist-item" v-if="music.image_url" :key="index">
                            <a @click="SelectItemToUser(music)">
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
                    </template>
                </template>
                <template v-if="!IsTabActive && user.favorite">
                    <template v-for="(music, index) in user.favorite">
                        <div class="playlist-item" v-if="music.image_url" :key="index">
                            <a @click="SelectItemToUser(music)">
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
                    </template>
                </template>
            </div>
        </div>
        <div class="bottom-listing">
            <div class="playlist-items">
                <div
                    class="playlist-item"
                    v-for="(music, index) in ItemToItemList"
                    :key="index"
                >
                    <a @click="SelectItemToItem(music)">
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
import token from "../utils/token"
import {apiUrls, authAjax} from "../store/api/urls";
import Ghost from "../components/Ghost";

export default {
    name: "HomePage",
    props: {msg: String},
    components: {
        Ghost,
    },
    data() {
        //Why does the return force me to put the { on the same line?????
        return {
            ItemToUserList: [],
            ItemToItemList: [],
            CurrentMusic: null,
            screenWidth: 0,
            enablePlayer: true,
            IsTabActive: true,
            moodValue: null,
            user: {},
        };
    },
    methods: {
        SendRating(value) {
            if (value === 'like') {
                authAjax()
                    .get(apiUrls.sendRating, {
                        params: {
                            user_id: 2,
                            item_id: this.$route.query.music_id,
                            rating: 1,
                        },
                    })
                    .then((response) => {
                        console.log(response.data)
                    })
            } else if (value === 'dislike') {
                authAjax()
                    .get(apiUrls.sendRating, {
                        params: {
                            user_id: 2,
                            item_id: this.$route.query.music_id,
                            rating: -1,
                        },
                    })
                    .then((response) => {
                        console.log(response.data)
                    })

            } else {
                console.log('error')
            }
        },
        AnimateButton(e) {
            e.preventDefault;
            //reset animation
            e.target.parentNode.classList.remove("animate");

            e.target.parentNode.classList.add("animate");
            setTimeout(function () {
                e.target.parentNode.classList.remove("animate");
            }, 1000);

        },
        ChangeTab(tab) {
            if (tab === "recomended") {
                if (this.IsTabActive === true) return;
                else this.IsTabActive = !this.IsTabActive;
            }
            if (tab === "favorite") {
                if (this.IsTabActive === false) return;
                else this.IsTabActive = !this.IsTabActive;
            }
        },
        AddToPlaylist() {
            const musicId = this.$route.query.music_id;
            authAjax().get(apiUrls.addToFavorite, {params: {item_id: musicId}})
                .then(() => {
                    this.getUser()
                })
        },
        Share() {
            const link =
                "https://www.facebook.com/sharer/sharer.php?u=" +
                "https://www.youtube.com/watch?v=" +
                this.$route.query.music_id;
            window.open(link, "_blank");
        },
        SelectItemToUser(music) {

            this.CurrentMusic = null;
            setTimeout(() => {
                this.CurrentMusic = music;
                this.$router.push({query: {music_id: music.video_id}});
                this.newItemToItemList(music);
            }, 1);
        },
        SelectItemToItem(music) {
            this.CurrentMusic = null;
            setTimeout(() => {
                this.CurrentMusic = music;
                this.$router.push({query: {music_id: music.video_id}});
                this.newItemToItemList(music);
            }, 1);

        },
        PlayerStateChange(event) {
            if (event && event.data === 0) {
                const index = this.ItemToUserList.findIndex((el) => {
                    //Here, this logic is wrong

                    return el.video_id === this.CurrentMusic.video_id;
                });
                if (this.ItemToUserList.length > index + 1) {
                    this.SelectItemToUser(this.ItemToUserList[index + 1]);
                }
            }
        },
        resizeEvent() {
            this.enablePlayer = false;
            setTimeout(() => {
                this.enablePlayer = true;
            }, 1);
            this.screenWidth = window.innerWidth;
        },
        newItemToItemList(item) {
            authAjax()
                .get(apiUrls.musicList, {
                    params: {
                        recom_type: "iti",
                        item_id: item.video_id,
                        number_of_items: 20,
                    },
                })
                .then((response) => {
                    this.ItemToItemList = response.data;
                });
        },
        playerReady() {
            this.$refs.player.unMute();
        },
        getInitialData(filter = "empty") {
            authAjax()
                .get(apiUrls.musicList, {
                    params: {
                        recom_type: "itu",
                        number_of_items: 20,
                        scenario: "main",
                        filter,
                    },
                })
                .then((response) => {
                    this.ItemToUserList = response.data;
                    this.CurrentMusic = null;
                    setTimeout(() => {
                        this.CurrentMusic = this.ItemToUserList.length
                            ? this.ItemToUserList[0]
                            : null;
                        if (this.CurrentMusic && this.CurrentMusic.video_id) {
                            this.$router.push({query: {music_id: this.CurrentMusic.video_id}});
                            this.newItemToItemList(this.CurrentMusic);
                        }
                    }, 1);
                });
        },
        getItemToUserList(music) {
            authAjax()
                .get(apiUrls.musicList, {
                    params: {
                        recom_type: "iti",
                        item_id: music.video_id,
                        number_of_items: 5,
                    },
                })
                .then((response) => {
                    this.ItemToUserList = response.data;
                });
        },
        getUser() {
            return authAjax()
                .get(apiUrls.getUserDetail)
                .then((response) => {
                    this.user = response.data;
                })
        },
        filterByMood() {
            if (this.moodValue) {
                this.getInitialData(this.moodValue)
            }
        },
        isFavorite(music) {
            if (music && music.video_id && this.user && this.user.favorite) {
                return this.user.favorite.find(el => el.video_id === music.video_id)
            }
            return false
        }
    },
    computed: {
        playerSize() {
            return this.screenWidth ? this.screenWidth : 0;
        },
        playerParameters() {
            return {autoplay: 1};
        },
    },
    mounted() {
        if (!token.isAuthorized) {
            this.$router.push({name: 'login'})
            return
        }
        this.getUser().catch(() => {
            this.$router.push({name: 'login'})
        });
        this.screenWidth = window.innerWidth;
        const music_id = this.$route.query.music_id;
        if (music_id) {
            this.SelectItemToItem({video_id: music_id});
            this.getItemToUserList({video_id: music_id});
        } else {
            this.getInitialData();
        }
    },
    watch: {
        $route(route) {
            const music_id = route.query.music_id;
            if (
                (!this.CurrentMusic && music_id) ||
                (music_id && music_id !== this.CurrentMusic.video_id)
            ) {
                this.SelectItemToItem({video_id: music_id});
            }
        },
    },
};
</script>


<style scoped>
/*
TODO LIST:
Add breakpoints

Turn dimensions into ratios
*/
.wrapper {
    border-top: 5px solid #c3073f;
    border-bottom: 5px solid #c3073f;
    border-radius: 7px;
    display: block;
    width: 200px;
    height: 40px;
    line-height: 40px;
    font-size: 18px;
    font-family: sans-serif;
    text-decoration: none;
    color: #ffff9b;
    letter-spacing: 2px;
    text-align: center;
    position: relative;
    transition: all .35s;
    align-self: center;
    margin-top: 15px;
    cursor: pointer;
}


.wrapper span {
    position: relative;
    z-index: 2;
}

.wrapper:after {
    position: absolute;
    content: "";
    top: 0;
    left: 0;
    width: 0;
    height: 100%;
    background: #ff003b;
    border-radius: 20px;
    transition: all .35s;
}

.wrapper:hover {
    color: #fff;
}

.wrapper:hover:after {
    width: 100%;
}

.tabs {
    display: flex;
    overflow: hidden;
    justify-content: center;
    height: 30px;
    background: #1b1b1b;
    border-radius: 5%;
    font-size: 1.2vw;
    text-align: center;
}

.tab-favorite {
    width: 30%;
    background: #960323;
    border: black solid 2px;
    border-radius: 20px;
    height: 80%;
    margin-left: 7%;
    cursor: pointer;
    align-self: center;
    overflow: hidden;
}

.tab-recomended {
    width: 30%;
    background: #960323;
    border: black solid 2px;
    border-radius: 20px;
    height: 80%;
    cursor: pointer;
    align-self: center;
    overflow: hidden;
}

.active {
    background: #ff2556;
    width: 29%;
}

.playlist-item a {
    cursor: pointer;
    display: block;

    /*these two are playing a huge role*/
    flex-grow: 1;
    flex-shrink: 1;

    min-width: 0px;
    text-decoration-color: rgb(3, 3, 3);
    text-size-adjust: 100%;
}

.playlist-item a:hover {
    background-color: #254f64;
    size: 20px;
    border-radius: 3px;
    cursor: pointer;
}

.playlist-item-listened {
    background-color: #254f64;
    size: 20px;
    border-radius: 3px;
    cursor: pointer;
}

.MainContainer {
    display: grid;
    grid-template-areas:
    "head head head"
    "left main right"
    "bottom bottom bottom";
    align-items: center;
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
    /*height: fit-content;*/
    height: 340px;
}

.music-player {
    display: flex;
    flex-direction: column;
}


svg,
.action-item img {
    position: relative;
    width: 70%;
    height: 100%;
    z-index: 10000;
}

.actions-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.action-item {
    margin: 5px;
    align-items: center;
    background-color: #e7e7e7;
    width: 35px;
    height: 35px;
    border-radius: 20px;
    cursor: pointer;
    transition: all .35s;
    position: relative;
    display: block;
    border: solid 2px rgba(9, 32, 71, 0.6);
}

.action-item:hover, .action-item.active {
    color: #fff;
}

.action-item:after {
    position: absolute;
    content: "";
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #c3073f;
    border-radius: 20px;
    transition: all .35s;

}

.action-item:hover:after, .action-item.active:after {
    height: 0;
}

.left-recommended {
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
    /* height: fit-content; */
    height: 470px;
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

.right-recommended {
    background-color: #262626;
    grid-area: right;
    display: flex;
    flex-direction: column;
    font-size: 10px;
    max-height: 460px;
    border-radius: 20px;
    border-top: 6px solid #c3073f;
    border-bottom: 6px solid #c3073f;
    color: #4e4e50;
    box-shadow: 5px 5px 10px 5px rgba(9, 32, 71, 0.6);
    margin-top: 24px;
    margin-bottom: 24px;

    /*height: fit-content;*/
    height: 470px;
}

.playlist-items {
    overflow-y: auto;
    height: 400px;
    font-size: 10px;
    display: block;
    margin-top: 10px;
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
    white-space: normal;
}

.bottom-listing {
    grid-area: bottom;
}

.bottom-listing .playlist-items {
    height: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fill, 400px);
    justify-content: space-around;
}

.bottom-listing .playlist-item {
    min-width: 300px;
}

.question-box {
    display: inline-block;
    font-size: 15px;
}

ul {
    list-style-type: katakana-iroha;
    width: fit-content;
    margin: 0 auto;
    text-align: left;
}

ul li {
    font-family: monospace, "lucida console";
    color: #05d9e8;
}

p,
label {
    font-family: monospace, "Lucida Console";
    font-style: oblique;
    color: #05d9e8;
}

ul li:hover {
    background-color: #254f64;
    size: 20px;
    border-radius: 3px;
    cursor: pointer;
}

.ghost {

}

@media (max-width: 880px) {
    .MainContainer {
        overflow: hidden;
    }

    .tabs {
        font-size: 1.8vw;
    }

    .bottom-listing {
        display: none;
    }

    .MainContainer {
        display: flex;
        flex-direction: column;
    }

    .right-recommended {
        min-width: 318px;
        width: 69%;
        height: fit-content;
    }

    .left-recommended {
        min-width: 318px;
        height: fit-content;
    }

    .center {
        order: -1;
        min-width: 318px;
        height: fit-content;
    }

    .ghost {
        display: none;
    }

    .question-box ul {
        margin: 0 auto;
        padding: 0;
        margin: 0 5px 0 5px;

    }

    li {
        display: inline;
    }

}

</style>