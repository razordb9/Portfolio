<script lang="ts">
    import { page } from '$app/stores';
</script>

<main class="container">
    <div class="error-container">
        <div class="error-msg">
            <h1>Upps an error occured</h1>
            <h1>{$page.error.message}</h1>
        </div>
    </div>
    
</main>