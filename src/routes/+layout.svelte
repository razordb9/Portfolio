<script lang="ts">
  import "$lib/css/custom_style.css";
  import "$lib/css/pico.min.css";
</script>

<html data-theme="dark" />
<head>
  <script src="https://kit.fontawesome.com/e2903f0fe1.js" crossorigin="anonymous"></script>
</head>
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
        <a href="https://github.com/razordb9" class="fa-brands fa-github"></a>
        |
        <a href="https://www.linkedin.com/in/thomas-hudson-zau%C3%9Fnig-76285a137/" class="fa-brands fa-linkedin"></a>
        |
        <a href="https://www.instagram.com/tsonga_64/" class="fa-brands fa-instagram"></a>
        |
        <a href="https://twitter.com/ThomasZaussnig" class="fa-brands fa-twitter"></a>

    </small>
</footer>
