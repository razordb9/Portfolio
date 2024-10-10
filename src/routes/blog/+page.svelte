<script lang="ts">
    import Blog from '$lib/Components/blog.svelte';
    export let data;
    console.log(data.posts);
</script>

<h1 class="page-heading">Blog</h1>
    <!-- <div class="page-subtext">
        <p>In this area you can find technical articles I try to write about.</p>
    </div> -->
<div class="blog">
    <div class="blog-container">
            {#each data.posts as post}
                <div class="blog-item">
                    <Blog path={post.path} title={post.meta.title} published={post.meta.date} subtext={post.meta.subtext} publisher={post.meta.publisher}/>
                </div>
            {/each}
    </div>
</div>

<style lang="scss">
    .page-subtext {
        text-align: center;
    }

    .blog {
        // background-color: yellow;
        .blog-container {
            margin-top: 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            grid-gap: 4rem;
            width: 100%;
            max-width: 1280px;
            margin: 0 auto;
            margin-bottom: 6rem;
        }

        .blog-item {
            // margin-top: 20px;
            // margin: 5px;
            // padding: 10px;
            border-bottom: 1px solid var(--nav_primary);
            // background-color: lightgreen;

            border: 1px solid lightgrey;
            border-radius: 10px;
            // justify-content: space-between;
            // width: 150px;
            // background-color: yellow;
            box-shadow: 10px 10px 5px lightgrey;
        }
        // .blog-item:hover {
        //     box-shadow: 10px 10px 5px lightgrey;
        // }
    }
</style>