<template>
    <DesignTest msg="Hello" />
</template>

<script>
import DesignTest from './components/DesignTest.vue'
export default {
    name: 'App',
    components: {
        DesignTest
    }
}
</script>

<style >
html *
{
    font-family: monospace, "Lucida Console" !important; 
	font-style: oblique;
	color: #05d9e8;
}  
body
{
    background-color:#262626
}
</style>