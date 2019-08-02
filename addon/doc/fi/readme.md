# Unicode-pistekirjoituksen syöttö #

* Tekijät: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Lataa [vakaa versio][1]

Tällä lisäosalla voit muuntaa tekstiä pistekirjoituksesta
(esim. 1345-1236-145-1) unicode-pistekirjoitusmerkeiksi. Voit  myös muuntaa
tekstiä nykyisen pistesyöttötaulukon mukaisesti.

Tämän erikoistuneen lisäosan tarkoituksena on Liblouis-taulukkojen
parantelun helpottaminen sekä automaattisten testien lisääminen niille. Tätä
ei enää tarvita NVDA 2017.3:ssa lisätyn Unicode-pistetaulukon vuoksi, sillä
sitä on mahdollista käyttää Unicode-pistekirjoituksen syöttämiseen. Tästä
lisäosasta voi kuitenkin olla edelleen apua normaalin tekstin muuntamisessa
Unicode-pistekirjoitukseksi tietyn syöttötaulukon mukaisesti.

## Käyttö

* Avaa unicode-tekstieditori (esim. Notepad++).
* Paina NVDA+Ctrl+U tai valitse NVDA:n Työkalut-valikosta
  Unicode-pistekirjoituksen syöttö.
* Valitse, koostuuko syötteesi pistekirjoituspisteistä
  (esim. 1345-1236-145-1) vai normaalista, nykyisen pistetaulukon
  (esim. Hollanti (Alankomaat) mukaisesta tekstistä.
* Syötä pistekirjoitusta numeerisessa muodossa tai normaalia tekstiä.
* Paina OK.
* Tarvittavat unicode-merkit kopioidaan leikepöydälle, josta voit liittää ne
  haluamaasi paikkaan.

## Muutokset versiossa 3.0

* Uusi ylläpitäjä: Leonard de Ruijter.
* Tämä lisäosa on yhteensopiva Python 3:n ja sen ansiosta myös NVDA 2019.3:n
  ja uudempien kanssa.
* Lisätty mahdollisuus Unicode-pistekirjoituksen luomiseen normaalista
  tekstistä nykyisen pistesyöttötaulukon mukaisesti.

## Muutokset versiossa 2.0

* Ohje on käytettävissä Lisäosien hallinnasta.

## Muutokset versiossa 1.1 ##

* Viivettä lisätty, jotta ilmoitukset kuuluvat oikein.
* Useita uusia käännöksiä lisätty.
* Lisätty Ohje-vaihtoehto NVDA:n Ohje-valikkoon.
* Lisätty valintaruutu, jolla voi valinnaisesti korvata
  pistekirjoitusvälilyönnin (merkki 0x2800) tavallisella välilyöntimerkillä.
* Pikanäppäimien uudelleenmäärittely on nyt mahdollista NVDA:n
  Syötekomennot-valintaikkunan Työkalut-kategoriasta.

## Muutokset versiossa 1.0 ##

* Ensimmäinen versio
* Uusi kieli: ranska

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
