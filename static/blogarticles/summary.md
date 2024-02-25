# WebDesigner

## Webseitenkonzeption und Projektmanagement

### Definition Webdesign

Unter Webdesign wird die visuelle, funktionelle und strukturelle Ausarbeitung von Webseiten verstanden. Der Webdesigner beschäftigt sich also mit dem Aufbau, der Gestaltung und der Nutzerführung einer Webseite.

Davon abzugrenzen ist die Webentwicklung. Diese bezeichnet die technische Seite der Webseite und umfasst die Verarbeitung, Aufbereitung und Speicherung von Daten.

Während Sie als Webdesigner sich demnach mit der grafischen Oberfläche und der Nutzererfahrung auseinandersetzten, kümmert sich der Webentwickler um die technischen Prozesse, die im Hintergrund ablaufen.

### Definition Webdesigner

Aufgaben des Webdesigners:

* Erstellung des Designs
* Überschneidung zum Mediendesign
* Bildbearbeitung
* In der Praxis auch häufige Tätigkeiten des Webentwicklers

Der Webdesigner ist in erster Linie ein Problemlöser. Er gestaltet das Netz und die Nutzerfahrungen und muss dabei flexibel auf die Dynamiken des Webs reagieren. Das Webdesign muss sich an die Bedürfnisse der Nutzer und die technischen Voraussetzungen anpassen. Daher muss der Webdesigner das Web sehr gut kennen

* Designprozess

Stift + Papier = erste Skizze. Mit Design Tools Mockups anfertigen und setzt Entwüre mit Software um. 

* Mediendesign

Sie müssen Bildbearbeitung meist selbst übernehmen und benötigen grundlegende Kenntnisse in den wesentlichen Gestaltungsprinzipien wie der Farbenlehre, Elemebtabstände und Typografie.  

* Technische Aufgaben

SEO, das Hosting von Webseiten und kleine Programmieränderungen. Deswegen benötigt der Webdesigner ein gewissen Knowhow in den gängigen Programmiersprachen. 





## Technische Umsetzung 1

HTML = Hyper Text Markup Language

Legt aussehen und Struktur der Website fest

### Aufbau einer HTML Datei

```HTML
<!DOCTYPE html>
<html lang="de">
    <head>
        <title>Seitentitel</title>
    </head>
    <body>
        <h1>Der Webdesigner Kurs</h1>
    </body>
</html>
```

### Wichtigsten HTML Tags

HTML-Codes sind nicht verschlüsselt und werden daher einfach als Klartext an den Browser übergeben und von diesem ausgewertet. Um die HTML-Struktur von Webseiten besser zu verstehen, kann es daher sehr hilfreich sein, sich eine beliebige Internetseite anzeigen lassen. Dazu reicht ein einfacher Rechtsklick auf der Seite, woraufhin man „Seitenquelltext anzeigen“ auswählen kann.

```
<h1> – <h7>
Das in diesem HTML-Tag steht für Heading, also für eine Überschrift. Die verschiedenen Größen werden über die Zahlen 1 bis 7 definiert.

<p>
P steht für paragraph, also für einen Textabschnitt.

<div> bzw. <span>
Diese HTML-Tags werden genutzt, um HTML-Elemente zu strukturieren. Sie können unendlich oft auf einer Webseite verwendet werden und dienen beispielsweise dazu, einzelne Strukturabschnitte kopieren.

<a>
Dieses HTML-Tag generiert eine Link-Verbindung auf eine andere Internetseite.

Zusätzlich zu den HTML-Tags können auch noch weitere Informationen angegeben werden. Diese so genannten Attribute sind Teile von HTML-Tags, die nach dem tatsächlichen Bezeichner des Tags kommen, aber vor der abschließenden Klammer stehen.
```

### CSS - Cascading Style Sheets

Während die HTML-Tags den Inhalt der Elemente definieren, geben die CSS-Befehle ihnen das entsprechende Aussehen. Damit wird das eigentliche Design Ihrer Seite in eine eigene Datei geschrieben.

### Erstellen einer CSS Datei

Mit CSS können Sie das Styling Ihrer Webseite auf verschiedene Weise verändern: Entweder erstellen Sie eine eigene CSS-Datei, die Sie dann in die Seite einbinden oder Sie fügen ein style-Attribut mit den entsprechenden Eigenschaften an der gewünschten Stelle ein. Alternativ kann das style-Element auch direkt in den Head eingefügt werden. Wichtig ist, dass der CSS-Befehl immer zwischen geschweiften Klammern stehen muss.

```html
<link rel="stylesheet" href="./sytle.css">
```

```css
body {
    background-color: yellow;
}
```

### Klassen und IDs
```css

HIML Tag ansprechen
body {
    background-color: yellow;
}

Klasse ansprechen
.heading {
    font-size: 27px;
}
ID ansprechen
#menu {
    background-color: red;
}

/* Kommentar * /
```

### Javascript

* Bringt dynamik in die Website
* Kann ähnlich wie CSS eingebunden werden
* Einbindung von lIbraries/frameworks
* Clientseitig - Niemals geheime Daten im Frontend Javascrpit
* NodeJS - Javascript im Background

```js
//JS einbinden
<script src=""></script>
```

Wenn Sie in einem HTML-Dokument einen Link einbinden, können Sie diesen mit CSS-Modifyern zwar verändern, aber die Funktion des Ganzen bleibt dennoch recht einfach: Der Link kann angeklickt werden und öffnet sich. Wenn Sie das Ganze etwas interaktiver gestalten wollen, benötigen Sie JavaScript.

JavaScript ist eine dynamische Programmiersprache, die im Browser Ihres Webseitenbesuchers ausgeführt wird. Sie ermöglicht Ihnen, die Aktionen Ihrer Nutzer an bestimmten Funktionen zu knüpfen: Klickt der Webseitenbesucher beispielsweise auf den oben erwähnten Link an, könnte sich ein Bild öffnen.

Javascipt Datei in HTML einbinden

---

```html
<script src="./index.js"></script>
```

### Was kann Javascript

Die Skriptsprache JavaScript sorgt also dafür, dass HTML-Elemente ihr Verhalten ändern – eine Funktion, die mittlerweile bei fast allen modernen Webseiten genutzt wird. Neben einfachen oder komplexeren Animationen kann damit auch die User Experience verbessert oder das Aussehen der Webseite verändert werden.

Die begrenzten Möglichkeiten von HTML und CSS werden also durch JavaScript dynamisch erweitert. Dennoch sollte man beim Programmieren bedenken, dass der Webseiten-Besucher die Ausführung von JavaScript in seinem Browser auch bewusst verhindern könnte. Auch wenn das eher die Ausnahme als die Regel darstellt, sollte die Webseite so aufgebaut sein, dass sie auch ohne JavaScript funktioniert und die Inhalte weiterhin dargestellt werden (vgl. Hahn, 2020).

Neben dem klassischen JavaScript werden heute auch oftmals sogenannte JavaScript-Bibliotheken verwendet. Zu den bekanntesten zählen jQuery (http://jquery.com) und React (https://reactjs.org/). jQuery enthält Effekt- und Funktionssammlungen, die Sie beim Gestalten Ihrer Webseite einbinden können (vgl. Rohles, 2017).

React ist hingegen die moderne Variante, um interaktive User Interfaces umzusetzen. Weiterhin gibt es noch sogenannte JavaScript-Frameworks, welche zusätzlich noch vorgefertigte Strukturen für die Entwicklung bieten wie z.B. VueJS (https://vuejs.org/) oder Angular (https://angular.io/).

### Arten von Variablen

Wir unterscheiden zwischen zwei verschiedene Arten von Variablen bzw. Deklarationen: Die ersten sind let-Variablen. Sie gelten nicht innerhalb des gesamten Codes, sondern nur im Rahmen eines umschließenden Blocks aus geschweiften Klammern.

```js
let name = "Max Mustermann";
```

Der zweite Typus sind const-Variablen. Formal betrachtet handelt es sich bei einer Konstante nicht wirklich um eine Variable, da dieser im Rahmen der Deklaration sofort ein Wert zugewiesen werden muss, weil dies zu einem späteren Zeitpunkt nicht mehr möglich ist. Auch const-Variablen sind auf die Umgebung eines Blocks aus geschweiften Klammern { } eingeschränkt.

```js
const name = "Max Mustermann";
```

Während const-Variablen sich also (bis auf wenige Ausnahmen) im Anschluss nicht mehr ändern lassen, können let-Variabeln auch im weiteren Verlauf noch geändert werden.

### Arten von Datentypen

* Primitives
    * Number
    * String
    * Boolean
    * Symbol

* Object
    * Function
    * Array
    * Date
    * RegEx

* Special
    * null
    * undefined

### Javascript Operatoren

* Arithmetic Operators
    * Addition +
    * Subtraction -
    * Multiplication *
	* Exponentiation (ES2016) **
    * Division /
    * Modulus (Division Remainder) %
    * Increment ++
    * Decrement --
* Assignment Operators
    * =	
    * +=
    * -=
    * *=
    * /=
    * %=
    * **=
* Comparison Operators
    * ==	equal to
    * ===	equal value and equal type
    * !=	not equal
    * !==	not equal value or not equal type
    * greater than >
    * less than <
    * greater than or equal to >=
    * less than or equal to <=
    * ?	ternary operator
* String Operators

* Logical Operators
    * &&	logical and
    * ||	logical or
    * !	logical not
* Bitwise Operators
    * &	AND	
    * |	OR	
    * ~	NOT	
    * ^	XOR	
    * <<	left shift <<
    * >>	right shift >>
    * unsigned right shift >>>
* Ternary Operators
* Type Operators


### Primtive Data Types / einfache Datentypen

```js
const int = 1;

const string = "Hallo THomas";

const boolT = true; // true = 1

const boolF = false; // false = 0
```
### Objekte/Zusammengesetzte Datentypen

Objekte werden in geschweiften Klammern { } definiert. Sie haben einen so genannten Key-Value-Part.

```js
const kunde = {
    name: "Max Mustermann"; // string
    Kontostand: 2000;       // integer
    istRegistriert: true;   // boolean
}
```
Mit functions, also Funktionen, besteht die Möglichkeit, verschiedenste Funktionalitäten zusammenzufassen und mehrfach aufzurufen, beispielsweise das Berechnen einer Summe. Funktionen werden immer in folgender Form angegeben: function Bezeichnung der Funktion. Functions bieten zusätzlich die Möglichkeit Parameter zu übergeben. Hierbei definieren wir innerhalb der Klammern beliebig viele Variablen (im Beispiel a und b) und können anschließend ganz normal mit diesen Variablen arbeiten. Um eine Funktion aufzurufen, wird zunächst der Name (im Beispiel “summe”) und danach zwei Klammern angegeben. Zwischen den Klammern müssen wir als nächstes die Parameter mit Werten befüllen.

```js
function summeOhneParameter() {
    return 10 + 10
}

function summeMitParameter(a, b) {
    return a + b
}

const summe1 = summeOhneParameter();
const summe2 = summeMitParameter(10, 10);
```

Zu den Objekten zählen auch so genannte Arrays. Dabei handelt es sich um eine Abfolge von verschiedenen Datentypen, die immer mit eckigen Klammern markiert werden. Um auf die Werte von einem Array zugreifen zu können, müssen wir immer den Index angeben. Dieser startet bei einem Array immer bei 0.

```js
const transaktion = [10, 20, 30, 40];

const ersteTransaktion = transaktion[0];
const zweiteTransaktion = transaktion[1];
const dritteTransaktion = transaktion[2];
const vierteTransaktion = transaktion[3];
```

<img src="./assets/WBD-Modul5-Abb14.jpg">

### PHP

Ursprünglich bedeutete PHP zunächst „Personal Home Page“, jetzt steht es jedoch für PHP: Hypertext Preprocessor. Es handelt sich um eine Open Source-Skriptsprache, welche besonders gut für die Webprogrammierung geeignet ist. HTML, CSS und JavaScript stellen gemeinsam das Frontend dar, PHP bildet das Backend.

Während statische HTML-Seiten bereits fertig auf dem Server liegen, wird der PHP-Code zuerst von einem Programm ausgeführt. Dadurch wird die Webseite erzeugt und an den Browser gesendet. „Der Client erhält also nur das Ergebnis der Skriptausführung, ohne dass es möglich ist herauszufinden, wie der eigentliche Code aussieht“.

PHP ermöglicht also die dynamische Erzeugung von Inhalten und bietet ihnen damit viele Möglichkeiten, die JavaScript nicht hat. Dazu zählen insbesondere all die Veränderungen, die mit der Sicherheit Ihrer Internetseite zu tun haben, z.B. Login- oder Logout-Funktionen.

Außerdem ist es möglich, sich bei der Programmierung mit PHP mit einer Datenbank zu verbinden und die dort abgespeicherten Informationen abzurufen und zur Erstellung von Inhalten auf der eigenen Internetseite zu nutzen. Diese dynamische Erzeugung von Webinhalten erfolgt über so genannte Content Management Systeme (siehe Abschnitt CMS), die häufig in PHP programmiert sind.

Um mit PHP zu arbeiten, ist es notwendig, einen PHP-Interpreter zu nutzen. Dafür gibt es bei Windows, Mac oder auch Linux eigene Softwarepakete, die neben dem PHP-Interpreter auch entsprechende Datenbanken und Webserver umfassen.

### Anforderungen um PHP zu verwenden
* PHP Interpreter
* Lokale Entwicklung: LAMPP, XAMPP, MAMP

## Verwendet PHP
* Wordpress
* Joomla
* Drupal
* Lavarel
* Symfony Framework

### Funktionsweise
* Code wird von oben nach unten abgearbeitet
* Request -> Response Cycle
* Grundsätzlich Ähnlichkeit zu JavaScript
* Website kann nicht mehr einfach im Browser geöffnet werden
* Theoretisch kann HTML und PHP gemischt werden -> nicht empfohlen

PHP Response Cycle
<img src="./assets/PHP_ResponseCycle.png">

### Das erstellen einer PHP Datei

Da sich HTML und PHP kombinieren lassen, ist diese Markierung wichtig, um beide Teile voneinander abgrenzen zu können. Neben der Ausgabe von HTML steht Ihnen auch noch das dynamische Generieren von Bildern, PDF-Dateien und Flashanimationen zur Verfügung.

```php
<?php

?>
```

Wie in JavaScript gibt es auch bei PHP verschiedene Datentypen, Datenstrukturen und Variablen. Der größte Unterschied besteht darin, dass Variablen in PHP immer mit einem Dollarzeichen gekennzeichnet werden: $variablenname.

Weiterhin muss im Anschluss an Bezeichnungen oder Funktionsaufrufe immer ein Semikolon (;) folgen, da sonst eine Fehlermeldung ausgegeben wird.

```php
<?php
    $string = "Hello";

    $integer = 10;

    $boolean = true;

    $array = [10, 20, 30, 40];
?>

```

### PHP lokal nutzen

* Install MAMP/LAMP/XAMPP
* Terminal -> php -S localhost:8000

### PHP Libaries

Package manager for PHP is "Composer".
https://getcomposer.org

## CMS (Content Management System)

* Inhaltswartung für Webseiten
* Unterschiedliche Systeme je nach Anforderungen
* Ermöglicht "nicht Entwicklern" 'nderungen an der Website vorzunehmen
* Erweiterung durch Plugins
* Designvorlagen durch Templates 

### Klassische CMS Systeme
* Wordpress
* Drupal
* Joomla
* TYPO3

### Headless CMS
* CMS und Frontend sind voneinander unabhängig
* Können auf unterschiedlichen Servern betrieben werden -> Skalierung
* Unterschiedliche Technologien für Frontend und CMS

### Anbieter von Headless CMS
1. strapi
1. directus
1. contentful

Wordpress for Docker
https://github.com/nezhar/wordpress-docker-compose

### Start with Wordpress

WP-User: thomashz
WP-Password: yj_fb9-E

* Create a child theme
    * wp-content
    * themes
    * theme name
        * style.css add comment block

```js
/*
Theme Name: HSB Theme
Description:
Author:
Author URl: 
Template:
Version:
*/
```

        * create function.php (copy from existing theme)


## Technische Umsetzung II

### Animationen
* Aufmerksamkeit auf bestimmte Elemente legen
* Längere Aufmerksamskeitspanne der Webseitenbesucher
* Emotionen wecken

### Interaktionen bei Benutzereingaben
* Reaktion auf Benutzereingaben (Scroll, Klick, Bewegung, Hover)
* Mikrointeraktionen
* 
* 

### Interaktionen ohne Benutzereingaben
* Bringen Bewegung in die Webseite
* Lenken Fokus auf animierte Elemente
* Slider, Lade-Animation


### Umsetzung
* Für einfache Animationen reicht üblicherweise HTML/CSS
* Pseudo klassen (hover, active)
* Transition Eigenschanft

### Umsetzung komplexe Animationen
* HTML/CSS/JS
* Vanilla Javascript
* Externe Library
https://gsap.com
https://animejs.com



### CSS Animation mit Keyframes
* Ermöglicht komplexere Animationen ohne JS
https://www.w3schools.com/cssref/css3_pr_animation-keyframes.php


### Pseudo Klassen
https://w3schools.com/css/css_pseudo_classes.asp


### Important links
https://github.com/hsb-akademie/webdesigner-kurs


### Hosting und Performance

* Performance einer Webseite hat direkten Einfluss auf folgende Werte
    * Conversion Rate
        * Nutzer fürhen eine gewünschte Tätigkeit aus (z.B Newsletter Anmeldujg, Produktkauf, etc.)
        * Sinkt pro Sekunde Wartezeit um durchschnittlich 7%
        * Conversion Rate kann demnach durch gute Performance gesteigert werden
    * Sichtbarkeit
        * Seit 2017 werden nicht responsive Webseiten und schlechte Performance von Google im Suchindex benachteiligt
        * Performance spielt in SEO auch eine Rolle
    * Performance prüfen
        * https://developers.google.com/speed/pagespeed/insights/
        * Google Chrome Lighthouse
    * Nutzerfreundlichkeit

* Wichtige Metriken
    * FCP - First Contentful Paint
    * time to Interactive - Zeit bis Webseite voll funktionsfähig ist
    * FID - First Input Delay - zeit bis das erste Mal mit der Webseite interagiert werden kann

* Performance optimieren
    * Bilder komprimieren
    * CSS/JS komprimieren
    * CSS/JS nachladen
    * CDN (Content Delivery Network) verwenden (Cloudflair)
    * Serverseitigen Code optimieren bzw. bei Wordpress Plugins verwenden
    * Besseres Hostingpaket bzw. Datencenter in der Nähe der Nutzer wählen
    * Externe Ressourcen minimieren

* Vorgehen bei bestehender Webseite
    * Performance Analyse
    * Bottlenex identifizieren
    * Entsprechende Aktion wählen und Vorgang wiederholen

* Vorgehen bei neuen Webseiten
    * Maximalwerte für Metriken am Start des Projekts festlegen
    * Während der Entwicklung die nötigen Aktionen treffen, um über diesen Schwellenwert zu bleiben

Hosting

* Webserver für unsere Webseite
* Beeinflusst maßgeblich die Performance der Webseite
* Möglichkeiten
    * Eigener Server
    * Shared hosting
    * Cloud Anbieter

* Shared Hosting
    * Einfachste und kostengünstiges Möglichkeit des Hostings
    * Für kleine bis mittelgroße Projekte
    * Meistens all in one Paket
    * Überlicherweise Monats/Jahresabo

* Cloud Anbieter
    * AWS, Google Cloud, MS Azure
    * nahezu unlimitierte Ressourcen
    * Ab mittelgroßen Projekten
    * Wartungsintensiver als Shared Hosting
    * Abrechnung nur nach genutzer Leistung
    * ACHTUNG: Preise werden üblicherwese pro Stunde abgerechnet

Anbieter für Hosting
* AWS Lightsail
* domaintechnik.at
* Domain Factory df.eu
* all-inkl.com

Ich hab schon recht viel Vorahnung, aber gerade im Design eben keine. Da wollte ich mich etwas weiterbilden. 
Naja, ich finde den Kurs so lala. Den Design Part fand ich gut, weil ich da nicht viel wusste und viel gelernt habe. Den Rest finde ich jetzt nicht so grandios, um ehrlich zu sein. Sehr oberflächlich, aber was will man schon in 1h an HTML jemandem beibringen…


## 29.11.2023 Dozentenstunde

gohugo.io für statische Webseiten generieren

Projektmanagement
* Jira
* Asana

## 06.12.2024 IT Sicherheit

Bei Software oder was auch immer im besten Fall mindestens zwei Admin Accounts einrichten, um die volle Handlungsfreiheit zu haben.

### Passwortmanager verwenden!!!

Für Registrierungen/Zugangsdaten/Dienste/Services immer eine eigene Email Adresse verwenden z.B. Programmierung@beispiel.com , Registrierung@beispiel.com oder Technik@beispiel.com. Niemanls eine Email Adresse verwenden auf die mehrere Benutzer zugriff haben. 

Mit einem Passwort Manager kann man mit Mausklick Passwörter generieren und muss sich somit nicht alle Kundenpasswörter merken.

Angst -> das ungewisse / abstrakt (Gefahr)
Furcht -> konkret (Risiko)

EW x MT x SE \
Eintrittswahrscheinlichkeit x Mortalitäts Rate x  Subjektive Empfinden

SE ist der wichtigste Faktor in dieser Formel.

### Versagen
* TV technisches Versagen
* OV organisatorisches Versagen
* MV menschliches Versagen

TV - kommt selten vor\
OV - was passiert wenn man einen USB Stick findet (Eset Virusscan)\
MV - großteil der Unfälle sind in der Regel auf MV zurück zu verfolgen

DSGVO - Externe HDD oder USB Sticks inventarisieren ansonsten kann man Strafen zahlen
Alles was Daten speichern/verarbeiten kann, muss inventarisiert werden.

Emails verschlüsselt verschicken.\
https://snappass.symplasson.de/


## 13.12.2023 Webseitenpflege & Controlling (Update, Backups, Google Analytics)

### Webseitenpflege

1. Aktualisierung
1. Verantwortlichkeit
1. Sicherheit
1. Abhängigkeiten

Back WP Up for Wordpress backups

### Tracking
* Matomo
* Google Analytics (nicht DSVGO konform)

https://www.datenschutz-eprivacy.de/google-analytics-rechtlich-sicher-machen/

## 20.12.2023 Ziele & Zielgruppen

### Marketing is key

Lastschriftmandat ist sehr wichtig

Für Gründung eines Gewerbe ist keine explizite Ausbildung notwending. Daher ist es auch ein offenes Gewerbe und kann von jedem ausgeführt werden. Folgende freie Gewerbe können dafür gewählt werden:
* Automatisierte Datenverarbeitung
* Marketing und Kommunikation

Brand Personality Quiz Hausübung

## 10.01.2024 Projektmanagement

### KI

Game Theory -> Endliche, Endlose Spiele

### Projekt vs. Prozess

Was definiert ein Projekt?
* Neu
* Klares Ziel
* Zeithorizont
* Ressourcen
* Komplexität

Webseite ca. alle 5 Jahre neu um auf neue Technik/Systeme umstellen.

### Projektinhalt bzw. -partner

Anfrage - Briefing - Lastenheft - Angebot - Pflichtenheft - Umsetzung - Abschluss u Auswertung - Rechnung

1/3 bei Unterschrift 
1/3 bei Qualitätsschleife
1/3 bei Rechnung


## 17.01.2024 Webseitenaufbau & -typen

Tools für Pageflow
* Hotjar
* LeadInfo

### Webseitentypen
* Corporate Website
* Portfolio
* Shop
* Blog
* Landingpage
* Microsite
* Web-Apps
* Newsletter

Honeybot

## 31.01.24 Webseitenaufbau und Gestaltung

1. Urheberrecht
1. Domainrecht
1. Impressum
1. Datenschutz
1. Cookies
1. Zusammenfassung

Datenschutz- und AGB Generatoren verwenden für den Anfang einer neugründung

## 21.02.24 Gestaltungs- und Screendesign

Gestaltungsgrundsätze
* Gesetze der Nähe
* Gesetze der Ähnlichkeit
* Gesetz der Geschlossenheit
* Gesetz der Prägnanzk
* Gesetz der Konsistenz
* Gesetz der Erfahrung
* Gesetz der Kontinuität