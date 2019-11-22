# Unos brajice u unikod formatu (UnicodeBrailleInput) #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Preuzmi [stabilnu verziju][1]

Ovaj dodatak omogućuje konvertiranje teksta iz brajice
(npr. 1345-1236-145-1) u brajeve unikod znakove. Tekst je moguće
konvertirati i prema trenutačnoj brajevoj tablici za unos.

Svrha ovog specijaliziranog dodatka je pomoć pri izradi testova za liblouis
tablice, kao i za automatske testove za tvoj jezik. Dodavanjem brajeve
unikod tablice u NVDA 2017.3, ovaj dodatak za to više nije potreban, jer
korisnici mogu odabrati unos brajice pomoću nove tablice. Međutim, ovaj
dodatak i dalje može pomoći konvertirati normalni tekst u brajeve unikod
znakove, na osnovi određene tablice za unos.

## Primjena

* Otvori uređivač teksta koji prepoznaje unikod (na primjer Notepad plus
  plus).
* Pritisni NVDA+Ctrl+U ili odaberi „Unos brajice u unikod formatu” u NVDA
  izborniku Alati.
* Odaberi vrstu unosa: brajeve točke (npr. 1345-1236-145-1) ili normalni
  tekst prema trenutačnoj brajevoj tablici (npr. Hrvatski (Hrvatska).
* Tipkaj brajev tekst u numeričkom obliku, odnosno normalni tekst.
* Pritisni u redu.
* Potrebni unikod znakovi će se kopirati u međuspremnik, spremni za
  lijepljenje.

## Promjene u verziji 3.0

* Novi održavač: Leonard de Ruijter.
* Dodatak je kompatibilan s Python 3, a samim tim i s NVDA 2019.3 i novijim
  verzijama.
* Dodana je mogućnost generiranja brajice u unikod formatu iz normalnog
  teksta prema trenutačno odabranoj brajevoj tablici za unos.

## Promjene u verziji 2.0

* Pomoć za dodatak dostupna je u upravljaču za dodatke.

## Promjene u verziji 1.1 ##

* Poboljšano kašnjenje, kako bi se obavijesti mogle točno čuti.
* Puno novih prijevoda.
* Dodana dokumentacija u NVDA izborniku Pomoć.
* Dodan potvrdni okvir koji omogućuje opcionalnu zamjenu brajevog znaka za
  razmak (znak 0x2800) s normalnim znakom za razmak.
* Prečaci se sada mogu promijeniti koristeći NVDA dijaloški okvir ulaznih
  gesti, pod kategorijom Alati.

## Promjene u verziji 1.0 ##

* Prva verzija
* Novi jezici: francuski

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
