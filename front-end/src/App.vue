<template>
    <router-view/>
</template>

<script>
export default {
    name: 'App',
}
</script>

<style>
html * {
    font-family: monospace, "Lucida Console" !important;
    font-style: oblique;
    color: #05d9e8;
}

body {
    background-color: #262626
}

body::-webkit-scrollbar {
    width: 0;
}

body::-webkit-scrollbar-thumb {
    background-color: #c3073f;
}

body::-webkit-scrollbar-track {
    background-color: #262626;
}

</style>