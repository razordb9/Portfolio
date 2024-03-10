<script lang="ts">
    import Blog from '$lib/Components/blog.svelte';
    export let data;
    console.log(data.posts);
</script>
<h1 class="page-heading">Blog</h1>
    <div class="page-text">
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

<style>
    ul {
        list-style-type: none;
    }
</style>