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
      <img src="/Logo.png" alt="Hudson-Zaußnig Solutions" width="250" height="auto">
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
    .nav-links {
      display: none;
    }

    .nav-burger-menu .mobile {
      display: block;
    }
    .nav-burger-menu {
      margin-right:10px;
      display: inline-block;
      position: relative;
    }

    .nav-burger-menu-links {
      display: none;
      height: 220px;
      width: auto;
      background-color: var(--nav_primary);
      position: absolute;
      min-width: 160px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
      z-index: 1;
      right: 0; /* Align dropdown to the right */
      list-style-type: none;

      .nav-item {
        margin-bottom:20px;
        padding: 20px;
        background-color: green;

        a{
          text-decoration: none;
          border-radius: 5px;
          padding-inline: 1rem;
          color: var(--nav_secondary);
        }
        &:hover {
          a{
            background-color: var(--nav_secondary);
            color: var(--nav_primary);
          }
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