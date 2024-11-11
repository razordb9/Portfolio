<h1 class="page-heading">Test</h1>
<div class="page-subtext">
    <p>In this area you can find test stuff I try about.</p>
</div>
<!-- <ul class="flex-list">
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul> -->

<!-- Calendly Inline-Widget Beginn -->
<div class="calendly-inline-widget" data-url="https://calendly.com/thomas-zaussnig/30min" style="min-width:320px;height:700px;"></div>
<svelte:head>
  <script type="text/javascript" src="https://assets.calendly.com/assets/external/widget.js" async></script>
</svelte:head>
<!-- Calendly Inline-Widget Ende -->

<style>
.flex-list {
  list-style-type: none; /* Removes bullets */
  display: flex;         /* Applies Flexbox layout */
  padding: 0;            /* Removes default padding from the list */
  margin: 0;             /* Removes default margin */
  justify-content: space-between;
}

.flex-list li {
  margin-right: 20px;    /* Adds some spacing between items */
    background-color: yellow;
}
</style>