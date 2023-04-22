# UnicodeBrailleInput #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* Baixar [versão estável][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## Utilização:

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Pressione ok
* Os caracteres unicode necessários serão copiados para a área de
  transferência, prontos para serem colados.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Mudanças para 2.0

* A ajuda do extra está disponível a partir do gestor de extras

## Mudanças para 1.1 ##

* Melhorou-se o atraso para permitir que os anúncios fossem  ouvidos
  correctamente.
* Adicionaram-se novas traduções
* Foi adicionada documentação ao menu do NVDA
* Adicionada uma caixa de selecção para, opcionalmente, substituir o  espaço
  braille (caractere 0x2800) pelo caractere de espaço regular.
* As teclas de atalho podem ser redefinidas, usando o menu de entrada de
  comandos

## Mudanças para 1.0 ##

* Versão inicial
* Novo idioma: francês

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
