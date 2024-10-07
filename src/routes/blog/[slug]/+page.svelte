<script lang="ts">
    export let data;
</script>

<article>
    <h1>{data.title}</h1>
    <p>Published: {data.date}</p>
    <svelte:component this={data.content} />
</article>

<style lang="scss">
    ul {
        list-style-type: circle;
    }
    article {
        // background-color: yellow;
        margin: auto 20px;
    }

    code {
        background-color: lightgray;
    }

    pre {
        background-color: yellow;
        list-style-type: none;
    
    }
</style>