<script lang="ts">
    export let data;
</script>

<article>
    <div class="article-header">
        <h1>{data.title}</h1>
        <div class="date">Published: {data.date}</div>
        <div>{data.publisher}</div>
    </div>
    <div class="article-text">
        <svelte:component this={data.content} />
    </div>
</article>

<style lang="scss">
    
    ul {
        list-style-type: circle;
    }
    article {
        // background-color: lightgray;
        padding: 20px;

        .article-header {
            height: 100px;
            background-color: lightgrey;
            text-align: center;
            margin: auto 0;

            h1 {
                font-size: 35px;
            }
        }

        .article-text {
            margin-top: 20px;
        }
    }

    code {
        background-color: lightgray;
    }
</style>