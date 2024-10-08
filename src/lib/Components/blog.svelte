<script lang="ts">
    // import blogarticle from "$lib/Components/blogarticle.svelte";
    // export let post;
    export let path: string = "";
    export let title: string = "";
    export let published: string = "";
    export let subtext: string = "";
    export let publisher: string = "";
</script>

<!-- <img class="blog-item-img" src="/Logo.png" alt="Hudson-Zaußnig Solutions"> -->
<div class="blog-card">
    <div class="blog-card-title">
        <a href={path}>{title}</a>    
    </div>
    
    <div>
        <!-- <img class="blog-item-creator" src="/Thomas.jpg" alt="Thomas Hudson-Zaußnig"> -->
    </div>
    <div class="blog-card-publisher">
        by {publisher} {published}
    </div>
    <div class="blog-card-subtext">
        {subtext}
    </div>
</div>

<style lang="scss">
    .blog-card {
        margin-bottom: 20px;
        .blog-card-title {
            font-size:30px;
        }
        a {
            text-decoration-color: var(--nav_primary);
            color: black;
        }
        // a:hover{
        //     color: var(--nav_primary);
        // }

        img {
            max-width: 250px;
            width: 100%;
        }
        .blog-card-subtext {
            margin-top: 20px
        }
        .blog-card-publisher {
            color: var(--nav_primary);
        }
    }
</style>