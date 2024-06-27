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
        width: 70%;
        margin: 30px auto;
        text-align: end;
        background-color: var(--nav_primary);
        color: var(--nav_secondary);
        padding: 20px;
        
        a {
            text-decoration: none;
            color: var(--nav_secondary);
        }
        .footer-img {
            filter: invert(1); 
        }

        span{
            display: flex;
            flex-direction: row;
            justify-content: flex-end;
            gap: 10px;
        }
    }
</style>