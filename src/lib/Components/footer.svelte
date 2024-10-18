<footer>
    <div id="footer-content">
        Copyright &copy; Thomas HUDSON-ZAUSSNIG •
        <a href="/impressum">Impressum •</a>
        <a href="/agb">AGB •</a>
        <a href="/kontakt">Kontakt</a>
    </div>
    <span>
        <a href="https://github.com/razordb9" target="_blank"><img class="footer-img" src="/github.svg" alt="Github"/></a>
        <a href="https://www.linkedin.com/in/thomas-hudson-zau%C3%9Fnig-76285a137/" target="_blank"><img class="footer-img" src="/linkedin.svg" alt="LinkedIn"/></a>
        <a href="https://www.instagram.com/tsonga_64/" target="_blank"><img class="footer-img" src="/instagram.svg" alt="Instagram"/></a>
        <a href="https://twitter.com/ThomasZaussnig" target="_blank"><img class="footer-img"src="/twitter.svg" alt="Twitter"/></a>
    </span>
</footer>

<style lang="scss">
    footer {
        position: relative;
        width: 100%;
        text-align: center;
        background-color: var(--brand);
        color: var(--surface-1-light);
        padding: 20px;
        height: 80px;
        a {
            text-decoration: none;
            color: var(--surface-1-light);
        }
        .footer-img {
            filter: invert(1); 
        }

        span{
            margin-top: 10px;
            display: flex;
            flex-direction: row;
            justify-content: center;
            gap: 10px;
        }
    }
</style>