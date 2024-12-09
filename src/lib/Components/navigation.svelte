<script lang="ts">
  // import {Routes} from "$lib/Components/routes";

  type Route={
    path:string,
    name:string
  }

  var open = false;
  const openBurgerMenue = (e:MouseEvent) => {
    console.log(e.target)
    console.log(open)
    open = !open;
  }

  type Routes = Array<Route>;

  export let routes: Routes;
</script>
<nav class="navbar">
  <a href="/" class="logo">
      <img src="/Logo.png" alt="Thomas Hudson-Zaussnig" width="250" height="auto">
  </a>
  <ul class="nav-links">
    {#each routes as route}
      <li class="nav-item"><a href="{route.path}">{route.name}</a></li>
    {/each}
  </ul>
   <!-- svelte-ignore a11y-click-events-have-key-events -->
   <div class="nav-burger-menu" on:click={openBurgerMenue}> 
    <div class="line"></div>
    <div class="line"></div>
    <div class="line"></div>
    <ul class="nav-burger-menu-links" class:mobile={open==true}>
      {#each routes as route}
        <li class="nav-item"><a href="{route.path}">{route.name}</a></li>
      {/each}
    </ul> 
  </div>
  

</nav>
<style lang="scss">
  .navbar {
    width: 100%;
    height: 70px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--brand);
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
  .nav-burger-menu {
      display: none;
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
        color: var(--nav_secondary);
        border-radius: 5px;
        background-color: var(--surface-1-light);
      }

      &:hover {
        a {
          // background-color: var(--nav_secondary);
          transition: all 200ms ease-in-out;
          color: var(--nav_primary);
        }
      }
    }
  }

  @media (max-width: 600px) {
    .nav-links {
      display: none;
    }

    .nav-burger-menu .mobile {
      display: block;
    }
    .nav-burger-menu {
      margin-right:10px;
      display: inline-block;
    }

    .nav-burger-menu-links {
      flex-direction: column;
      display: none;
      top: 60px;
      position: absolute;
      height: auto;
      width: 100%;
      background-color: var(--brand);
      right: 0; /* Align dropdown to the right */
      margin: 10px 0;
      padding: 10px 0;

      .nav-item {
        margin: 10px;
        text-align: center;
        list-style-type: none;

        a{
          font-size: 1.2rem;
          text-decoration: none;
          color: white;
        }
      }
    }

    .line {
      width: 25px;
      height: 3px;
      background-color: #fff;
      margin: 3px;
    }
  }
</style>