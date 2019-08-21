# Entrada unicode para braille #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* baixe a [versão estável][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## Como usar

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* Pressione OK.
* Serão copiados para a área de transferência os devidos caracteres unicode
  prontos para serem colados.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## Mudanças na 2.0

* A ajuda do complemento está disponível no gestor de complementos.

## Mudanças na 1.1 ##

* Aumentada a espera para possibilitar ouvir-se corretamente os anúncios.
* Muitas traduções novas.
* Adicionada documentação no menu Ajuda do NVDA.
* Adicionada uma caixa de seleção para substituir opcionalmente o espaço
  braille (caractere 0x2800) pelo caractere de espaço regular.
* Os atalhos agora podem ser reatribuídos usando o diálogo de gestos para
  entrada do NVDA, na categoria ferramentas.

## Mudanças na 1.0 ##

* Versão inicial
* Novo idioma: Francês

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
