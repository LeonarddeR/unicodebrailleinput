# UnicodeBrailleInput #

* Авторы: Mesar Hameed, Patrick Zajda.
* загрузить [стабильную версию][1]
* загрузить [разрабатываемую версию][2]

Это дополнение позволяет конвертировать текст из Брайля (например
1345-1236-145-1) в Unicode символы Брайля.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language. With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required, as users can choose to input braille with the new table.

## Использование ##

* Откройте Юникод текстовый редактор (например, Notepad Plus Plus)
* Нажмите NVDA+Ctrl+U или выберите Ввод брайлевского юникода из меню NVDA
  сервис
* Введите текст Брайля в числовой форме.
* Нажмите OK.
* Требуемые Unicode символы будут скопированы в буфер обмена готовые для
  вставки.

## Изменения для 2.0 ##

* Справка дополнения доступна в диспетчере дополнений.

## Изменения для 1.1 ##

* Уменьшена задержка, чтобы позволить правильно услышать объявления.
* Многие новые переводы.
* Добавлено документация в меню справки NVDA.
* Добавлен флажок для необязательной замены пробела брайля (символ 0x2800)
  на регулярный символ пробела.
* Горячие клавиши теперь могут быть переназначены с помощью диалога ввода
  жестов NVDA в подкатегории Сервис.

## Изменения для 1.0 ##

* первоначальный релиз
* Новый язык: французский

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi

[2]: https://addons.nvda-project.org/files/get.php?file=ubi-dev
