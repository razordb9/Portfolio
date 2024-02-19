<script lang="ts">
  import "$lib/css/custom_style.css";
  import Footer from "$lib/Components/footer.svelte";
  import Navigation from "$lib/Components/navigation.svelte";
  import { routes } from "$lib/Components/routes";
</script>
<html lang="en"/>
<header>
  <Navigation routes={routes}>
  </Navigation>
</header>
<div id="page-container">
  <div id="content-wrap">
    <slot />
  </div>
</div>
<Footer />  

