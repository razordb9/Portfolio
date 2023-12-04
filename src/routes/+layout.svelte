<script lang="ts">
  import "$lib/css/custom_style.css";
  // import "$lib/css/pico.min.css";
  import Footer from "$lib/Components/footer.svelte";
  import Navigation from "$lib/Components/navigation.svelte";
  import { routes } from "$lib/Components/routes";
</script>

<html lang="en"/>
<head>
  <!-- <script src="https://kit.fontawesome.com/e2903f0fe1.js" crossorigin="anonymous"></script> -->
</head>
<header />
<main class="container">
  <Navigation routes={routes}>

  </Navigation>

  <slot />
  <Footer />

</main>

