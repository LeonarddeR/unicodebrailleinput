# Unicode盲文输入 #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* 下载 [稳定版][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## 使用方法

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* 按OK。
* 所需的unicode字符将被复制到您的剪贴板以供您粘贴。

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## 2.0更新日志:

* 插件帮助可从附加组件管理器获得。

## 版本1.1 ##

* 改善延迟以允许公告被正确听取。
* 许多新的翻译。
* 在NVDA帮助菜单下添加文档。
* 添加了一个复选框，可以用常规空格字符替换空格盲文（字符0x2800）。
* 现在可以使用Tools类别下的NVDA手势输入对话框重新分配快捷键。

## 1.0更新日志 ##

* 发布初始版本
* 新增法语翻译

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
