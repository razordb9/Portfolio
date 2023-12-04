<script lang="ts">
  // import {Routes} from "$lib/Components/routes";

  type Route={
    path:string,
    name:string
  }

  type Routes = Array<Route>;

  export let routes: Routes;
</script>
<nav class="navbar">
    <a href="/" class="logo">
        <img src="/Logo.png" alt="Hudson-Zaußnig Solutions">
    </a>
    <ul class="nav-links">
      {#each routes as route}
        <li class="nav-item"><a href="{route.path}">{route.name}</a></li>
      {/each}

    </ul>
</nav>