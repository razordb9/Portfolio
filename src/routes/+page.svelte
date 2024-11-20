<script lang="ts">
    import ContactForm from '$lib/Components/contact.svelte';
</script>

<section id="welcome-section">
    <h1>Hello I am Thomas</h1>
    <p>a ongoing webdesigner</p>
    <!-- <div class="item"><a href="/about">About me</a></div> -->
    <!-- <div class="item"><a href="/blog">Blog</a></div> -->

</section>
<ContactForm />


<style lang="scss">
    #contact {
        background-color: #303841;
        height: calc(100% - 80px);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        .contact-header {
            text-align: center;
            color: white;
            margin-top: 100px;
        }

        .contact-header p {
            font-size: 2rem;
        }

        .contact-links {
            margin-top: 20px;
            color: white;
        }
        form {
            width: 70%;
            position: relative;
            margin-inline: auto;
            margin: 100px auto;
            color: white;
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
            box-shadow: 0px 6px 15px -5px rgba(0, 0, 0, 0.25);

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
            p{
                color:var(--surface-2);
            }
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
            color: black;
            border-radius: 4px;
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
        
    }
    #welcome-section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: var(--surface-5);
        
        width: 100%;
        height: 100vh;

        .item{
        display: flex;
        justify-content: center;
        align-items: center;
        list-style: none;
        //   height: 50%;
        // margin-right: 10px;
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
    }
    
</style>