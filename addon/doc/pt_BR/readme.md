# Entrada Braille Unicode (UnicodeBrailleInput) #

* Autores: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* baixe a [versão estável][1]

Esse complemento permite converter texto de braille (por exemplo,
1345-1236-145-1) em caracteres Braille Unicode. Você também pode converter
texto de acordo com a tabela braille de entrada atualmente selecionada.

O objetivo deste complemento especializado é facilitar a melhoria das
tabelas liblouis e adicionar testes automáticos ao seu idioma. Com a adição
da tabela braille unicode no NVDA 2017.3, esse complemento não é mais
necessário, pois os usuários podem optar por inserir braille com a nova
tabela. No entanto, esse complemento ainda pode ajudar na conversão de texto
normal em braille unicode, de acordo com uma tabela de entrada específica.

## Como usar

* Abra um editor de texto compatível com unicode (por exemplo, Notepad++).
* Pressione NVDA+Ctrl+U ou escolha Entrada Braille Unicode encontrada no
  menu de Ferramentas do NVDA.
* Selecione se sua entrada consiste em pontos braille (por exemplo,
  1345-1236-145-1) ou texto normal de acordo com a tabela braille atual (por
  exemplo, Holandês (Holanda)).
* Digite seu texto braille em forma numérica ou em texto normal,
  respectivamente.
* Pressione OK.
* Serão copiados para a área de transferência os devidos caracteres unicode
  prontos para serem colados.

## Mudanças na 3.0

* Novo mantenedor: Leonard de Ruijter.
* O complemento é compatível com Python 3 e, portanto, com o NVDA 2019.3 e
  superiores.
* Foi adicionada a capacidade de criar braille unicode a partir de texto
  normal, de acordo com a tabela braille de entrada atualmente selecionada.

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

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
