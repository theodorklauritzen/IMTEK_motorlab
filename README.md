# IMTEK_motorlab
A repository for a project in IMTEK

# Plan for utførelse av rapporten

- [X] Pakke ut zip filene
    - De er pakket ut, men må sorteres. Dessuten har vi ikek noe referanse, som gjør mange av dem ubrukelige.
- [X] Se over lysarkene for rapportskrivekruset til Øyvind
- [X] Finne ut hvordan vi koder kretsene så de blir fine
- [ ] Se over vurderingskriteriene
- [X] Lære Latex
- [ ] Se over oppgavearket for å se om vi har glemt noe
- [ ] Husk å se over alle målenheter, dette må samkjøres

# Outline

- [ ] Sammendrag
    - Hovedfokus på det vi har gjort og resultater
- [ ] Introduksjon
    - Nødvendig teori
    - Deler som bør være med
        - P- og PI-regulatorer
    - Spesifikke spørsmål i oppgaven
        - Hvordan vil motoren oppføre seg med de to regulatorene dersom vi påfører ytterligere belastning på motoren, for eksempel ved å bremse den med en finger?
        - Hva er ”jobben” til proporsjonal- og integraldelen? Altså, hvilken funksjon har de to i et reguleringssystem?
- [ ] Hastisghetsmåler (Dag 1) *@AnhoRhino*
    - Nødvendig teori
    - [Metode](#metode)
    - [Resultater](#resultater)
    - [Diskusjon](#diskusjon)
- [ ] Hastighetsregulator (Dag 2) *@theodorklauritzen*
    - Nødvendig teori
    - [Metode](#metode)
    - [Resultater](#resultater)
    - [Diskusjon](#diskusjon)
- [ ] Posisjonsmåler (Dag 2) *@theodorklauritzen*
    - Nødvendig teori
    - [Metode](#metode)
    - [Resultater](#resultater)
    - [Diskusjon](#diskusjon)
- [ ] Posisjonsregulator (Dag 3)
    - Nødvendig teori
    - [Metode](#metode)
    - [Resultater](#resultater)
    - [Diskusjon](#diskusjon)
- [ ] Konklusjon
    - Ny kunnskap so forsøket produserte
        - De viktigste resultatene
    

# Krav til utforming

- Bruk temasetninger i begynnelsen av hvert avsnitt

## Måleenheter

- Bruk denne kommandoen for half space: `\,`
- Husk at måleenheter ikke skal være i kursiv
- Bruk SIunits biblioteket

## Metode
- Ingen teori
- Presenter hva vi har gjort og hvordan vi har gjort det
- Beskriv implementasjonen

## Resultater
- Resultater
    - [Figurer](#figurer), [tabeller](#tabeller) og rentekst
        - Alle figurer og plots skal diskuteres
- Ikke påpek spesielle ting i resultatene, dette er [diskusjon](#diskusjon)
- Ikke gjenta metode beskrivelse

## Diskusjon
- Forklar eventuelle avvik fra forventingene
- Kan være hensiksmessig å slå sammen [resultater](#resultater) og diskusjon

## Figurer
- Alle figurer / plots skal diskuteres
- Figurnummer
- Figurtekst
    - Skal være under, ref Øyvind
- Tittel på plot
- Variabler, navn og måleenhet på aksene
- Skalering av aksene

## Tabeller
- Tabellnummer
- Tabelltekst
    - Over tabellen
- Måleenheter
- Design
    - Ingen vertikale linjer
    - Kun horisontale linjer over og under overskirften. Eventuelt også under selve tabellen.

## Likninger
- En liking er en del av teksten
- Skal ha lkningsnummer
    - **Unntak**: Mellomregninger som ikke refereres til i brødteksten
- Alle symboler skal forklares
- Tegnsetting på samme måte som i vanlige setninger.
    - Altså, hvis likningen er slutten på en setning, så skal det være et punktum på slutten.
- Referer til likninger med ´\\eqref´