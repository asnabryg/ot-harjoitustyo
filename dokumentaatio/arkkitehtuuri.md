# Arkkitehtuurikuvaus

## Rakenne
Koodin pakkausrakenne on seuraavanlainen:  
![Pakkausrakenne](./kuvat/Pakkausrakenne.png)

Pakkaus *ui* sisältää käyttöliittymästä, *game_logic* pelilogiikasta ja *repositories* tuloksien tallennuksesta vastaavan koodin.

## Käyttöliittymä
Käyttöliittymä sisältää kolme eri näkymää:
- Menu
- Peli näkymä
- Tulostaulu näkymän  

Jokaisen näkymän luominen tapahtuu eri luokissa. Näkymien näyttämisestä sekä käyttäjän syötteiden tarkistamisesta määrää [Userinterface](../2048/src/ui/ui.py)-luokka. Käyttöliittymän on eristetty pelilogiikkasta, se vain kutsuu pelilogiikan metodeja. Jokaisen pelilogiikka metodin kutsun jälkeen, ui koodi päivittää peliruudun.

## Pelilogiikka
Pelin logiikka ja laskenta tapahtuu [Game2048](../2048/src/game_logic/game2048.py)-luokassa.
