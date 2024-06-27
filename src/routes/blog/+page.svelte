<script lang="ts">
    import Blog from '$lib/Components/blog.svelte';
    export let data;
    console.log(data.posts);
</script>
<main>
    <h1 class="page-heading">Blog</h1>
        <div class="page-subtext">
            <p>In this area you can find technical articles I try to write about.</p>
        </div>
        <br>
    <div class="blog">
        <ul>
            <div class="blog-container">
                
                    {#each data.posts as post}
                        <li class="blog-item">
                            <Blog path={post.path} title={post.meta.title} published={post.meta.date} />
                        </li>
                    {/each}
            </div>
        </ul>
    </div>
</main>
<style lang="scss">
    ul {
        list-style-type: none;
    }

    .page-subtext {
        text-align: center;
    }

    .blog {
        .blog-container {
            display: flex;
            flex-wrap: wrap;
            // flex-direction: column;
            // justify-content: center;
        }

        .blog-item {
            // display:flex;
            flex: 1 1 calc(50% - 10px);
            margin: 5px;
            padding: 10px;
            border: 1px solid var(--nav_primary);
            border-radius: 5px;
        }
    }
</style>