<script lang="ts">
  import "$lib/css/custom_style.css";
  import Footer from "$lib/Components/footer.svelte";
  import Navigation from "$lib/Components/navigation.svelte";
  import { routes } from "$lib/Components/routes";
</script>

<main class="app">
  <header>
    <Navigation routes={routes}>
    </Navigation>
  </header>
  <slot />
</main>
<Footer /> 



<style lang="scss">
  .app{
    display:flex;
    flex-direction: column;
    min-height: calc(100vh - 80px);
    height: 100%;
  }
</style>