<script lang="ts">
  import { RMark } from '$lib/index';
  import { onMount } from 'svelte';
  
  const sampleText = 
  `
  # Header1
  
  ## Header 2 

  ### Header 3
  
  #### Header 4
  
  ##### Header 5
  
  ###### Header 6

  **Bold**
  *Italic*

  [Link](https://github.com/tlylt/rmark)

  This is **Bold** and this is *Italic*.

  __ This is Boold toooo __ 

  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ornare erat facilisis odio viverra gravida. Phasellus in finibus libero. Duis eget pellentesque arcu, ut lobortis mi. Praesent vitae nulla sed leo dignissim finibus eget hendrerit arcu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc vestibulum enim nibh, eu pellentesque tellus fermentum venenatis. Nam consectetur sem a magna mattis, sed luctus purus tincidunt. Nam faucibus tellus sed ligula molestie pulvinar. Mauris facilisis felis ex, eu tempor justo commodo et. Aenean lobortis dignissim diam eget tempor.

  Sed pellentesque nulla sit amet tincidunt sagittis. Phasellus eget justo nulla. Cras nisi odio, lobortis nec ante eget, commodo euismod
  turpis. Cras id orci dolor. Etiam auctor, nisl luctus volutpat lacinia, turpis orci euismod magna, pharetra eleifend massa metus aliquet
  `;
  //![Image](https://raw.githubusercontent.com/tlylt/rmark/main/static/logo.svg)
  

  let isClient = false;

  onMount(() => {
    const page = document.getElementById("page");
    page.innerHTML = new RMark().render(sampleText);
  });

//   if (isClient) {
//     console.log(testing)
//     // const page = document.getElementById("page");
//     // page.innerHTML = new RMark().render(sampleText);
//   }


</script>

{#if isClient}
  <!-- Client-side specific code -->
  <script>
    // Access the document object here
    console.log(document);
  </script>
{/if}

<h1 class="page-heading">just for testing</h1>
<div id="page"></div>