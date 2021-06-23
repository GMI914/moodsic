<template>
  <legend>Login</legend>
  <p>Username</p>
  <input type="text" v-model="LoginData.username"/>
  <p>Password</p>
  <input type="password" v-model="LoginData.password"/>
  <button  @click="Login" >Proceed</button>
</template>

<script>
import { ajax, apiUrls } from "../store/api/urls";

export default {
  data(){
    return{
      LoginData:{
        username:'' ,
        password:'',
      }
    }
  },
  methods:{
    Login(){
      ajax.post(apiUrls.loginUser,this.LoginData).then(response=>{console.log(response.data)})
    }

  }
}
</script>

<style scoped>

input[type="text"],
input[type="password"] {
  display: block;
  padding: 4px;
  box-sizing: border-box;
  border: 2px solid #c3073f;
  background-color: #254f64;
  border-radius: 4px;
  font-size: 21px;
  font-family: monospace, "Lucida Console";
  color: #ffff9b;
  width: 55%;
  margin: 3px auto 9px;
}

button {
  background-color: #c3073f;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin: 20px auto 0px;
  width: 40%;
}

p {
  font-family: monospace, "Lucida Console";
  font-style: oblique;
  color: #05d9e8;
  font-size: 0.8em;
  margin: 5px 0px 0px 10px;
  text-align: center;
}

legend {
  font-family: monospace, "Lucida Console";
  font-style: oblique;
  font-size: 2em;
  font-weight: 300;
  line-height: 0.5em;
  text-align: center;
  color: #4dc3fa;
  text-shadow: 2px 2px red;
  margin-bottom: 20px;
}
</style>
