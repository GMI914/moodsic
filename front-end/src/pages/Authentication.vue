<template>
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
</template>

<script>
import Register from "../components/Register";
import Login from "../components/Login";

export default {
  components: {
    Register,
    Login,
  },
  data() {
    return {
      screenWidth: 0,
      OK: "IxWo7yG-W-E",
    };
  },
  mounted() {
    this.screenWidth = window.innerWidth;
  },
  methods: {
    playerReady() {
      this.$refs.player.unMute();
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
};
</script>

<style scoped>
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
  min-height: 350px;
  height: fit-content;
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
  min-height: 350px;
  height: fit-content;
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
  height: fit-content;
}

@media (max-width: 1080px) {
  .MainContainer {
    display: block;
  }
  .center {
    display: none;
  }
}
</style>