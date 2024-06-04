<script lang="ts">
    // import blogarticle from "$lib/Components/blogarticle.svelte";
    // export let post;
    export let path: string = "";
    export let title: string = "";
    export let published: string = "";
</script>

<!-- <img class="blog-item-img" src="/Logo.png" alt="Hudson-Zaußnig Solutions"> -->
<div class="blog-card">
    <div class="blog-card-title">{title}</div>
    <a href={path}>{title}</a>
    <div>
        <!-- <img class="blog-item-creator" src="/Thomas.jpg" alt="Thomas Hudson-Zaußnig"> -->
        <span>By</span>
        Thomas HZ 
        <span> {published}</span>
    </div>
</div>
<style lang="scss">
    .blog-card {
        // background-color: blue;
        border: 2px solid var(--nav_primary);
        border-radius: 5px;
        padding: 5px;
        margin: 20px auto;

        .blog-card-title {
            font-size:30px;
        }
        a {
            text-decoration: none;
            color: black
        }
    }
</style>