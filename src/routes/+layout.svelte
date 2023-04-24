<script lang="ts">
  import "$lib/css/custom_style.css";
  import "$lib/css/pico.min.css";
</script>

<html data-theme="dark" />
<header />
<main class="container">
  <nav>
    <ul>
      <li><strong>Thomas Hudson Zaussnig</strong></li>
    </ul>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="#">About</a></li>
      <!-- <li><a href="#" role="button">Button</a></li> -->
    </ul>
  </nav>

  <slot />
</main>

<footer>
    <small>
        Copyright &copy; Thomas HUDSON-ZAUSSNIG •
        <a href="/impressum">Impressum</a>
        <a href="/kontakt">Kontakt</a>
        <a href="https://github.com/razordb9" class="fa-brands fa-github">Github</a>
    </small>
</footer>
