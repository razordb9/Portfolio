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
    </div>
    <span>By</span>
    Thomas HZ 
    <span> {published}</span>
</div>

<style lang="scss">
    .blog-card {
        margin-bottom: 20px;

        .blog-card-title {
            font-size:30px;
        }
        a {
            // text-decoration: none;
            color: black
        }
        a:hover{
            color: var(--nav_primary);
            text-decoration: underline;
        }

        img {
            max-width: 250px;
            width: 100%;
        }
    }
</style>