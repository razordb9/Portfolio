<script lang="ts">
    import ContactForm from '$lib/Components/contact.svelte';
    export let data;
    console.log(data.image);
</script>

<article>
    <div class="article-header">
        <h1>{data.title}</h1>
        <div class="date">Published: {data.date}</div>
        <div>{data.publisher}</div>
        {#if data.image != ""}
            <img src={data.image} alt="testing"/>
        {/if}
        <div class="article-tags">
            {#each data.categories as category}
	    		<span class="surface-4 category">&num;{category}</span>
		    {/each}
        </div>
    </div>
    <div class="article-text">
        <svelte:component this={data.content} />
    </div>
</article>
<ContactForm question='You have something to tell me?'/>

<style lang="scss">
    article {
        // background-color: lightgray;
        padding: 20px;

        .article-header {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            flex-direction: column;
            border-radius: 5px;
            height: auto;
            background-color: var(--primary);
            color: var(--surface-1-light);
            text-align: center;
            margin: auto 0;
            padding: 20px 0px;
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
            // margin: auto 0;
        }

        .article-tags > * {
            padding: var(--size-2) var(--size-3);
            border-radius: 50px;
        }
    }

</style>