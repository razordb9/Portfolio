<script lang="ts">
    import { page } from '$app/stores';
</script>

<main class="container">
    <h1>Upps an error occured</h1>
    <h1>{$page.error.message}</h1>
</main>