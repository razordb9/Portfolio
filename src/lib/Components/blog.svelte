<script lang="ts">
    export let path: string = "";
    export let title: string = "";
    export let published: string = "";
    export let subtext: string = "";
    export let publisher: string = "";
    export let image: string = "";

    if (image.length == 0){
        image = "https://cdn.freecodecamp.org/testable-projects-fcc/images/tribute.jpg";
    }
</script>

<!-- <img class="blog-item-img" src="/Logo.png" alt="Hudson-Zaußnig Solutions"> -->
<div class="blog-card">
    <a href={path}>
        <img
            class="blog-image"
            src='{image}'
            alt="{image}"
        />
        <div class="blog-meta">
            <div class="blog-card-title">
                {title}    
            </div>
            <div class="blog-card-subtext">
                {subtext}
            </div>
            <div class="blog-card-publisher">
                <div>{published}</div>
                <div>{publisher}</div>
            </div>
        </div>
    </a>
</div>

<style lang="scss">
    .blog-card {
        margin-bottom: 20px;
        a {
            // text-decoration-color: var(--nav_primary);
            // color: black;
            text-decoration: none;
        }

        .blog-image {
                height: calc(100% - 6.8rem);
                width: 100%;
                object-fit: cover;
                border-radius: 10px 10px 0px 0px;
            }
        .blog-meta {
            padding: 10px;
            color: black;
            .blog-card-title {
                font-size:30px;
                color: var(--nav_primary);
            }
            
            .blog-card-subtext {
                margin-top: 20px
            }
            .blog-card-publisher {
                color: lightgrey;
                margin-top: 10px
            }
        }
    }
</style>