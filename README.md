# Ohjelmistotekniikka, harjoitustyö

Tämä projekti toimii Helsingin yliopiston kurssin Ohjelmistotekniikka, kevät 2021 harjoitustyönä.

# 2048 peli
Projekti on yleinen 2048 pulmapeli. Pelissä liu'utetaan numeroituja laattoja ja yritetään yhdistää saman numeroiset laatat. Tavoitteena on saada laatta, jonka numero on 2048 tai enemmän 4x4 kokoisella pelialueella. Pelissä tallentuu parhain pistemäärä omalle paikalliselle koneelle.

## Python-versio
Peli toimii 3.6.0 tai siitä uudemmalla Python-versiolla

## Dokumentaatio
- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimuusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Lataa projektin viimeisin [lähdekoodi](https://github.com/asnabryg/ot-harjoitustyo/releases) valitsemalla *Assets*-osion alta *2048_source_code_*(versionumero).zip.

2. Mene kansioon **2048/** ja suorita seuraavat komennot siellä.


3. Asenna kaikki riippuvuudet komennolla:

```bash
poetry install
```

4. Käynnistä peli komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot
Kommennot pitää suorittaa 2048/ kansion sisällä, jotta ne toimivat

### Pelin suorittaminen:
```bash
poetry run invoke start
```
### Testaus:
```bash
poetry run invoke test
```
### Testikattavuus:
```bash
poetry run invoke coverage-report
```
Raportti generoituu 2048/htmlcov/index.html tiedostoon.

### Pylint:
Suorittaa tiedoston [.pylintrc](./2048/.pylintrc) määrittelemät tarkistukset:
```bash
poetry run invoke lint
```

### Alusta tietokanta:
<sub>**HUOM!** Ei tarvitse itse alustaa pelin ensimmäisellä suorituskerralla.</sub>  
<sub>Peli alustaa itse sen, jos tiedostoa ei ole vielä luotu. Suorita komento vain, jos haluat nollata tietokannan kokonaan.</sub>

```bash
poetry run invoke initialize-db
```
