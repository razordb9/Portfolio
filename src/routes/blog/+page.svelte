<script lang="ts">
    import Blog from '$lib/Components/blog.svelte';
    export let data;
    console.log(data.posts);
</script>

<h1 class="page-heading">Blog</h1>
    <div class="page-subtext">
        <p>In this area you can find technical articles I try to write about.</p>
    </div>
<div class="blog">
    <ul>
        <div class="blog-container">
                {#each data.posts as post}
                    <li class="blog-item">
                        <Blog path={post.path} title={post.meta.title} published={post.meta.date} subtext={post.meta.subtext} publisher={post.meta.publisher}/>
                    </li>
                {/each}
        </div>
    </ul>
</div>

<style lang="scss">
    ul {
        list-style-type: none;
    }

    .page-subtext {
        text-align: center;
    }

    .blog {
        .blog-container {
            margin-top: 20px;
            display: flex;
            // flex-wrap: wrap;
            flex-direction: column;
            justify-content: space-between;
        }

        .blog-item {
            // display:flex;
            flex: 1 1 calc(50% - 10px);
            margin: 5px;
            padding: 10px;
            border-bottom: 1px solid var(--nav_primary);
            // border: 1px solid var(--nav_primary);
            // border-radius: 5px;
            // justify-content: space-between;
            // width: 150px;
            // background-color: yellow;
        }
    }
</style>