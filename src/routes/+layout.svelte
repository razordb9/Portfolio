<script lang="ts">
  import "$lib/css/custom_style.css";
  import Footer from "$lib/Components/footer.svelte";
  import Navigation from "$lib/Components/navigation.svelte";
  import { routes } from "$lib/Components/routes";
</script>
<html lang="en"/>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<header>
  <Navigation routes={routes}>
  </Navigation>
</header>
<body>
  <main>
    <slot />
  </main>
</body>
<Footer />  

