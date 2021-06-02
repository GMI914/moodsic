<template>
    <div class="container">
        <Ghost/>
        <div style='display:inline-block;'>
            <ul>
                <p>What's your mood?</p>
                <label>
                    <li><input name="mood" type='radio'>
                        <i>Mood1</i></li>
                </label>

                <label>
                    <li><input name="mood" type='radio'>
                        <i>Mood2</i></li>
                </label>

                <label>
                    <li><input name="mood" type='radio'>
                        <i>Mood3</i></li>
                </label>
            </ul>
        </div>
        <div class="wrapper">
            <router-link :to="{name:'home'}"><span>Proceed!</span></router-link>
        </div>
    </div>
</template>

<script>
import Ghost from "../components/Ghost";

export default {
    components: {
        Ghost
    }
}
</script>

<style scoped>
body {
    background-color: #262626;
}

.container {
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -64.5px;
    margin-top: -85.5px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

}

.wrapper {
    border-top: 5px solid #c3073f;
    border-bottom: 5px solid #c3073f;
    border-radius: 7px;
}

a {
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
}

a span {
    position: relative;
    z-index: 2;
}

a:after {
    position: absolute;
    content: "";
    top: 0;
    left: 0;
    width: 0;
    height: 100%;
    background: #ff003b;
    transition: all .35s;
}

a:hover {
    color: #fff;
}

a:hover:after {
    width: 100%;
}

ul {
    list-style-type: katakana-iroha;
}

ul li {
    font-family: monospace, "lucida console";
    color: #05d9e8;
}

p, label {
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
