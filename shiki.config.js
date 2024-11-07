// src/lib/shiki.js
import { createHighlighter, codeToHtml } from 'shiki';
let highlighter;

const shiki_langs = ['javascript', 'html', 'rust', 'typescript', 'json', 'yaml', 'css', 'scss', 'svelte', 'sql', 'bat'];
const shiki_themes = ['monokai', 'min-light', 'dracula', 'synthwave-84', 'material-theme', 'laserwave', 'vitesse-dark', 'everforest-dark', 'dark-plus', 'nord', 'dracula-soft', 'andromeeda', 'github-dark-dimmed', 'poimandres', 'solarized-dark'];

const themes = {
    dark: 'everforest-dark',
    light: 'min-light',
}

async function initHighlighter() {
    if (!highlighter) {
        highlighter = await createHighlighter({
            themes: shiki_themes,
            langs: shiki_langs
        });
    }
}

function appendLanguage(code, lang) {
    return `
        <div class="copy-button-wrapper">
            <span class="language-description">${lang}</span>
        </div>
        ${code}
    `
    // <button
    //             class="copy-button btn btn-square"
    //             aria-label="copy-codeblock"
    //             aria-live="polite"
    //             title="copy codeblock"
    //             type="button">
    //             <svg xmlns="http://www.w3.org/2000/svg"
    //                 width="24" height="24" viewBox="0 0 24 24"
    //                 stroke-linecap="round" stroke-linejoin="round"
    //                 class="lucide lucide-copy">
    //                 <rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/>
    //             </svg>
    //         </button>
}

function replaceRgbWithVar(code) {
    const regex = /#F8F8F2/g;
    // Replace each occurrence with 'var(--shiki-color)'
    const resultString = code.replace(regex, 'var(--shiki-color)');
    return resultString;
}

export async function highlightCode(code, lang = 'javascript') {
    if (!code) {
        //throw new Error('Code must be provided to highlight.');
        code = "js"
    }
    await initHighlighter();
    let highlighted = await codeToHtml(code, {
        lang: lang,
        themes: themes,
        // optional customizations
        cssVariablePrefix: '--shiki-',
    });
    let _code = replaceRgbWithVar(highlighted)
    console.log('xxxxxx', _code)
    let highlightedWithLang = appendLanguage(_code, lang);
    return highlightedWithLang;
}