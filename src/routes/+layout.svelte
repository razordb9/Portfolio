<script lang="ts">
  import "$lib/css/custom_style.css";
  import Footer from "$lib/Components/footer.svelte";
  import Navigation from "$lib/Components/navigation.svelte";
  import { routes } from "$lib/Components/routes";
  interface Props {
    children?: import('svelte').Snippet;
  }

  let { children }: Props = $props();
</script>

<header>
  <Navigation routes={routes}>
  </Navigation>
</header>
<main class="app">
  
  {@render children?.()}
</main>
<Footer /> 



<style lang="scss">
  .app{
    display:flex;
    flex-direction: column;
    min-height: calc(100vh - 80px);
    height: 100%;
    background-color: red;
  }
  @media (max-width: 500px){
    .app{
      // backgroundk-color: red;
      padding-inline: var(--side);
    }
  }

</style>