<script lang="ts">
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store';
  
    // Define writable stores for form fields
    const name = writable('');
    const email = writable('');
    const message = writable('');
    const formMessage = writable('');
  
    // Form submission handler
    async function handleSubmit(event: Event) {
      event.preventDefault();
  
      const formData = {
        name: $name,
        email: $email,
        message: $message
      };
  
      try {
        // Send data to the server via a POST request
        const response = await fetch('/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData)
        });
  
        const result = await response.json();
        formMessage.set(result.message || 'Thank you for contacting us!');
        if (response.ok) {
          name.set('');
          email.set('');
          message.set('');
        }
      } catch (error) {
        formMessage.set('An error occurred. Please try again later.');
      }
    }
  </script>
  
<div class="wrapper">
    <form on:submit={handleSubmit}>
        <label for="fullName">Vor und Nachname</label>
        <input type="text" id="fullName" name="fullName" bind:value={$name} required/>

        <label for="email">Email</label>
        <input
            type="email"
            id="email"
            name="email"
            placeholder="example@email.com"
            required
            bind:value={$email}
        />

        <label for="textArea">Nachricht</label>
        <textarea name="message" id="message" rows="10" cols="30" bind:value={$message} required/>

        <button type="submit">Senden</button>
    </form>
    {#if $formMessage}
      <p>{$formMessage}</p>
    {/if}
</div>

<style lang="scss">
    form {
        width: 70%;
        position: relative;
        margin-inline: auto;
        margin: 100px auto;
    }
    label {
        font-weight: 600;
    }
    .toast{
        display:block;
        width: 70%;
        margin-inline: auto;
        background-color: var(--surface-3);
        padding: 1rem 2rem;
        border-radius: .5rem;
        position: relative;
        .close{
            position: absolute;
            right: 0;
            top: 0;
            width:2rem;
            margin:.2rem;
            height: 2rem;
            background: var(--secondary);
            border:none;
            small{
                display: flex;
                flex-direction: center;
                align-items: center;
                height: 100%;
            }
        }
        /* color: whitesmoke; */
        p{
            color:var(--surface-2);

        }
        box-shadow: 0px 6px 15px -5px rgba(0, 0, 0, 0.25);

    }
    input[type="text"],
    input[type="email"],
    textarea {
        width: 100%; /* Full width */
        padding: 12px; /* Some padding */
        border: 1px solid #ccc; /* Gray border */
        border-radius: 4px; /* Rounded borders */
        box-sizing: border-box; /* Make sure that padding and width stays in place */
        margin-top: 6px; /* Add a top margin */
        margin-bottom: 16px; /* Bottom margin */
        resize: none;
    }
    button[type="submit"] {
        padding: 0.5rem 2rem;
        background-color: var(--surface-2);
        color: var(--surface-3);
        &:hover,
        &:focus,
        &:active {
            color: var(--surface-3);
        }
    }
    @media screen and (max-width: 768px) {
        form, .toast {
            width: 90%;
        }
    }
</style>
