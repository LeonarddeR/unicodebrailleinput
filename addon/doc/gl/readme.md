# UnicodeBrailleInput #

* Autores: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* descargar [versión estable][1]

Este complemento permíteche convertir texto de braille
(P.e.. 1345-1236-145-1) a caracteres braille Unicode. Tamén podes convertir
texto de acordo coa táboa braille de entrada actualmente seleccionada.

O propósito deste complemento especializado é facer máis doado axudar a
mellorar as táboas de liblouis e engadir probas automáticas para a túa
lingua. Coa incorporación de táboas braille unicode no NVDA 2017.3, este
complemento xa non se require, xa que os usuarios poden escoller introducir
braille coa táboa nova. Porén, este complemento aínda pode axudar a
convertir texto normal a braille unicode de acordo cunha táboa de entrada
concreta.

## Utilización

* Abrir un editor de textos que soporte unicode (por exemplo Notepad máis
  máis)
* Preme NVDA+Ctrl+U ou escolle Entrada de Braille Unicode atopada no menú
  ferramentas do NVDA.
* Selecciona se a se a túa entrada consiste de puntos braille
  (p.ex. 1345-1236-145-1) ou texto normal de acordo coa táboa braille actual
  (p.ex. Alemán -Países Baixos-).
* Escribe o texto braille en forma numérica ou o teu texto normal,
  respectivamente.
* Premer Aceptar.
* Os caracteres Unicode copiaranse no portapapeis listos para se pegar.

## Cambios para 3.0

* Novo mantedor: Leonard de Ruijter.
* O complemento é compatible con Python 3 e, en consecuencia, con NVDA
  2019.3 e superior.
* Engadida a posibilidade de crear braille unicode a partir de texto normal
  de acordo coa táboa braille de entrada actualmente seleccionada.

## Cambios para 2.0

* A axuda do complemento está dispoñible no Administrador de Complementos.

## Cambios para  1.1 ##

* Mellorado o retraso para permitir que os anuncios sexan escoitados
  corectamente.
* Moitas traducións novas .
* Documentación engadida o menú de axuda do NVDA.
* Engadidda unha caixa de verificación para reemplazar opcionalmente o
  espazo braille (carácter 0x2800) polo carácter de espazo.
* Os atallos poden agora ser transferidos mediante o diálogo de entrada
  xestos do NVDA, na categoría ferramentas.

## Cambios para 1.0 ##

* Versión inicial
* Novos Idiomas: Francés

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
