<template>
  <div class="MainContainer" v-if="IsLogedIn">
    <div class="left-recommended">
      <Ghost></Ghost>
      <div class="question-box">
        <p>
          How would you <br />
          describe the song?
        </p>
        <ul>
          <label>
            <li>
              <input name="describe the song" type="radio" /> <i>Happy</i>
            </li>
          </label>
          <label>
            <li>
              <input name="describe the song" type="radio" /> <i>Cheerful</i>
            </li>
          </label>
          <label>
            <li>
              <input name="describe the song" type="radio" /> <i>Gloomy</i>
            </li>
          </label>
          <label>
            <li><input name="describe the song" type="radio" /> <i>Sad</i></li>
          </label>
        </ul>
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
          <div class="action-item bubbly-button " @click="AddToPlaylist; AnimateButton($event)">
            <img src="../assets/like.svg" />
          </div>
          <div class="action-item bubbly-button " @click="AddToPlaylist; AnimateButton($event)">
            <img src="../assets/dislike.svg" />
          </div>
          <div class="action-item bubbly-button" @click="AddToPlaylist; AnimateButton($event)">
            <img src="../assets/heart.svg" />
          </div>
          <div class="action-item bubbly-button" @click="Share">
            <img src="../assets/share.svg" />
          </div>
        </div>
      </div>
    </div>
    <div class="right-recommended">
      <div class="tabs">
        <div
          class="tab-recomended bubbly-button"
          @click="ChangeTab('recomended')"
          :class="{ active: IsTabActive }"
        >
          Recomended
        </div>
        <div
          class="tab-favorite bubbly-button"
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
                    <img :src="music.image_url" />
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
        <template v-else>
          <template v-for="(music, index) in FavoritesList">
            <div class="playlist-item" v-if="music.image_url" :key="index">
              <a @click="SelectItemToUser(music)">
                <div class="thumbnail-meta-container">
                  <div class="thumbnail-container">
                    <img :src="music.image_url" />
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
                <img :src="music.image_url" />
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
  <div v-else>
    <div class="MainContainer">
      <div class="left-recommended">
        <Register></Register>
      </div>
      <div class="center">
        <youtube-iframe
          ref="player"
          :noCookie="true"
          :playerParameters="playerParameters"
          :player-width="playerSize / 3"
          :player-height="(playerSize * 3) / 16"
          :video-id="OK"
          @ready="playerReady"
        ></youtube-iframe>
      </div>
      <div class="right-recommended">
        <Login></Login>
      </div>
    </div>
  </div>
</template>

<script>
import { ajax, apiUrls } from "../store/api/urls";
import Ghost from "../components/Ghost";
import Register from "../components/Register";
import Login from "../components/Login";
import "../../design/bublebutton.scss";

export default {
  name: "DesignTest",
  props: { msg: String },
  components: {
    Ghost,
    Register,
    Login,
  },
  data() {
    //Why does the return force me to put the { on the same line?????
    return {
      ItemToUserList: [],
      ItemToItemList: [],
      FavoritesList: [],
      CurrentMusic: null,
      screenWidth: 0,
      enablePlayer: true,
      IsTabActive: true,
      IsLogedIn: true,
      OK: "IxWo7yG-W-E",
      
    };
  },
  methods: {
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
      console.log(musicId);
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
        this.$router.push({ query: { music_id: music.video_id } });
        this.newItemToItemList(music);
      }, 1);
    },
    SelectItemToItem(music) {
      this.CurrentMusic = null;
      setTimeout(() => {
        this.CurrentMusic = music;
        this.$router.push({ query: { music_id: music.video_id } });
        this.newItemToItemList(music);
      }, 1);
      ajax
        .get(apiUrls.musicList, {
          params: {
            recom_type: "itius",
            // user_id: null,
            item_id: music.video_id,
            number_of_items: 20,
          },
        })
        .then((response) => {
          this.ItemToUserList = response.data;
          this.ItemToUserList.filter((el) => el.video_id === music.video_id);
          this.ItemToUserList.unshift(music);
        });
    },
    Getfavorite(music) {
      this.CurrentMusic = null;
      setTimeout(() => {
        this.CurrentMusic = music;
        this.$router.push({ query: { music_id: music.video_id } });
        this.newItemToItemList(music);
      }, 1);
      ajax
        .get(apiUrls.musicList, {
          params: {
            recom_type: "itius",
            // user_id: null,
            item_id: music.video_id,
            number_of_items: 5,
          },
        })
        .then((response) => {
          this.FavoritesList = response.data;
          this.FavoritesList.filter((el) => el.video_id === music.video_id);
          this.FavoritesList.unshift(music);
        });
    },
    PlayerStateChange(event) {
      if (event && event.data === 0) {
        const index = this.ItemToUserList.findIndex((el) => {
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
      ajax
        .get(apiUrls.musicList, {
          params: {
            recom_type: "iti",
            item_id: item.video_id,
            number_of_items: 50,
          },
        })
        .then((response) => {
          this.ItemToItemList = response.data;
        });
    },
    playerReady() {
      this.$refs.player.unMute();
    },
    getInitialData() {
      ajax
        .get(apiUrls.musicList, {
          params: {
            recom_type: "itu",
            // user_id: null,
            number_of_items: 20,
          },
        })
        .then((response) => {
          this.ItemToUserList = response.data;
          this.CurrentMusic = this.ItemToUserList.length
            ? this.ItemToUserList[0]
            : null;
          if (this.CurrentMusic) {
            this.$router.push({
              query: { music_id: this.CurrentMusic.video_id },
            });
            this.newItemToItemList(this.CurrentMusic);
          }
        });

      /*Here we want to also get the list of favorites*/
    },
  },
  computed: {
    playerSize() {
      return this.screenWidth ? this.screenWidth : 0;
    },
    playerParameters() {
      return { autoplay: 1 };
    },
  },
  mounted() {
    this.screenWidth = window.innerWidth;
    const music_id = this.$route.query.music_id;
    if (music_id) {
      this.Getfavorite({ video_id: music_id });
      this.SelectItemToItem({ video_id: music_id });
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
        this.SelectItemToItem({ video_id: music_id });
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
  background: #ff2556;
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
  background: #ff2556;
  border: black solid 2px;
  border-radius: 20px;
  height: 80%;
  cursor: pointer;
  align-self: center;
  overflow: hidden;
}

.active {
  background: #960323;
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
  height: 400px;
}

.music-player {
  display: flex;
  flex-direction: column;
}

svg,
.action-item img {
  width: 70%;
  height: 100%;
}

.actions-wrapper {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.action-item {
  margin: 5px;
  align-items: center;
  background-color: #c3073f;
  width: 35px;
  height: 35px;
  border-radius: 20px;
  cursor: pointer;
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
  height: 350px;
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
  height: 350px;
}

.playlist-items {
  overflow-y: auto;
  height: 333px;
  font-size: 10px;
  display: block;
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
  justify-content: space-between;
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
</style>