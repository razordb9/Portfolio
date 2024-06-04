<script lang="ts">
  // import {Routes} from "$lib/Components/routes";

  type Route={
    path:string,
    name:string
  }

  var open = false;
  const openBurgerMenue = (e:MouseEvent) => {
    console.log(e.target)
    open = !open;
  }

  type Routes = Array<Route>;

  export let routes: Routes;
</script>
<nav class="navbar">
  <a href="/" class="logo">
      <img src="/Logo.png" alt="Hudson-Zaußnig Solutions" width="250" height="auto">
  </a>
  <ul class="nav-links">
    {#each routes as route}
      <li class="nav-item"><a href="{route.path}">{route.name}</a></li>
    {/each}
  </ul>
  <!-- <div class="nav-burger-menu" on:click={openBurgerMenue}>
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
    <ul class="nav-burger-menu-links" class:mobile={open==true}>
      {#each routes as route}
        <li class="nav-item"><a href="{route.path}">{route.name}</a></li>
      {/each}
    </ul> 
  </div> -->
  

</nav>
<style lang="scss">
  .navbar {
    width: 100%;
    height: 70px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--nav_primary);
    // padding: 10px 5px;

    .logo {
      display: flex;
      width: 250px;
      height: 100%;

      img {
        width: 100%;
        object-fit: contain;
        height: auto;
      }
    }
  }

  .nav-links {
    width: auto;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;

    .nav-item{
      display: flex;
      justify-content: center;
      align-items: center;
      list-style: none;
      height: 50%;
      margin-right: 10px;

      a{
        display: flex;
        padding-inline: 1rem;
        align-items: center;
        height: 100%;
        text-decoration: none;
        transition: all 200ms ease-in-out;
        // background-color: green;
        color: var(--nav_secondary);
        border-radius: 5px;
        background-color: rgb(119, 0, 0);
      }

      &:hover {
        a {
          background-color: var(--nav_secondary);
          transition: all 200ms ease-in-out;
          color: var(--nav_primary);
        }
      }
    }
  }

  @media (max-width: 600px) {
    
  }
</style>