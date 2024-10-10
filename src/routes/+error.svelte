<script lang="ts">
    import { page } from '$app/stores';
</script>

<div class="error-msg">
    <img src="error.png" alt="error"/>
    <h1>Upps an error occured</h1>
    <h1>{$page.error.message}</h1>
</div>

<style lang="scss">
    .error-msg {
        text-align: center;
        margin: auto 0;
    }
</style>