<script lang="ts">
    import blogarticle from "$lib/Components/blogarticle.svelte";
    // export let post;
    export let path: string = "";
    export let title: string = "";
    export let published: string = "";
</script>
<div class="blog-container">
    <div class="blog-item">
        <img src="/Logo.png" alt="Hudson-Zaußnig Solutions">
        <div>{title}</div>
        <button><a href={path}>More</a></button>
        <div>
            <img class="blog-item-creator" src="/Thomas.jpg" alt="Thomas Hudson-Zaußnig">
            <span>By</span>
            Thomas HZ 
            <span> {published}</span>
        </div>
    </div>
</div>