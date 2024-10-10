<script lang="ts">
    export let data;
</script>

<article>
    <div class="article-header">
        <h1>{data.title}</h1>
        <div class="date">Published: {data.date}</div>
        <div>{data.publisher}</div>
        <div class="article-tags">
            {#each data.categories as category}
	    		<span class="surface-4">&num;{category}</span>
		    {/each}
        </div>
    </div>
    <div class="article-text">
        <svelte:component this={data.content} />
    </div>
</article>

<style lang="scss">
    

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

        .article-tags {
            display: flex;
            gap: var(--size-3);
            margin-top: var(--size-7);
	    }

        .article-tags > * {
            padding: var(--size-2) var(--size-3);
            border-radius: var(--radius-round);
        }
    }

</style>