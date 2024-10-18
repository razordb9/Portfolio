<script lang="ts">
    import Project from '$lib/Components/projects.svelte';

</script>

<section id="welcome-section">
    <h1>Hallo ich bin Thomas</h1>
    <p>ein Webdesigner</p>
    <div class="item"><a href="/about">About me</a></div>
  </section>

<style lang="scss">
    #welcome-section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: var(--surface-5);
        
        width: 100%;
        height: 100vh;
    }

    .item{
      display: flex;
      justify-content: center;
      align-items: center;
      list-style: none;
    //   height: 50%;
      margin-right: 10px;

      a{
        display: flex;
        padding-inline: 1rem;
        align-items: center;
        height: 100%;
        text-decoration: none;
        transition: all 200ms ease-in-out;
        color: var(--nav_secondary);
        border-radius: 5px;
        background-color: var(--surface-1-light);
      }
    }
</style>