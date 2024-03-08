<script lang="ts">
    import Blog from '$lib/Components/blog.svelte';
    export let data;
    console.log(data.posts);
</script>
<div class="blog">
    <h1 class="page-heading">Blog</h1>
    <div class="page-text">
        <p>Here you can find all the projects which I already finished or which are in progress</p>
    </div>
    <!-- <Blog /> -->
    <br>
    <ul>
        {#each data.posts as post}
            <li>
                <Blog path={post.path} title={post.meta.title} published={post.meta.date} />
            </li>
        {/each}
    </ul>
</div>

<style>
    ul {
        list-style-type: none;
    }
</style>