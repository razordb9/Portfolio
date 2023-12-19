<div class="wrapper">
    <form>
        <label for="fullName">Vor und Nachname</label>
        <input type="text" id="fullName" name="fullName" />

        <label for="email">Email</label>
        <input
            type="email"
            id="email"
            name="email"
            placeholder="example@email.com"
        />

        <label for="textArea">Nachricht</label>
        <textarea name="message" id="message" rows="10" cols="30" />

        <button type="submit" value="Submit">Senden</button>
    </form>
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
