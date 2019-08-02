# UnicodeBrailleInput #

* Authors: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* تحميل: [الإصدار النهائي][1]

This add-on allows you to convert text from braille (E.G. 1345-1236-145-1)
to Unicode braille characters.  You can also convert text according to the
currently selected input braille table.

The purpose of this specialized addon is to make it easier to help to
improve liblouis tables and to add automatic tests for your language.  With
the addition of unicode braille table in NVDA 2017.3, this add-on is no
longer required for this, as users can choose to input braille with the new
table.  However, this add-on can still aid in converting normal text to
unicode braille according to a particular input table.

## الاستخدام

* Open a unicode aware text editor (for example Notepad++).
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu.
* Select whether your input consists of braille dots (e.g. 1345-1236-145-1)
  or normal text according to the current braille table (e.g. Dutch
  (Netherlands).
* Type your braille text in numeric form or your normal text, respectively.
* اضغط زر موافق.
* سيتم نسخ الأحرف التي كتبتها في صورة رقمية بطريقة شفرة البرايل الموحدة مما
  يمكنك لصقها في أي مكان.

## Changes for 3.0

* New maintainer: Leonard de Ruijter.
* Add-on is compatible with Python 3 and therefore with NVDA 2019.3 and
  above.
* Added the ability to create unicode braille from normal text according to
  the currently selected input braille table.

## مستجدات الإصدار 2.0

* إمكانية الوصول لملف المساعدة من مدير الإضافات البرمجية

## مستجدات الإصدار 1.1 ##

* تحسين التأجيل للسماح بالاستماع للرسائل بطريقة صحيحة.
* ترجمة الإضافة للعديد من اللغات.
* إضافة ملف تعليمات الإضافة ضن قائمة المساعدة ب NVDA.
* إضافة مربع تحديد لاستبدال المسافة البرايل اختياريا (الحرف 0x2800) بحرف
  المسافة القياسي.
* يمكن للمستخدم تعديل مفاتيح الاختصار الخاصة بالإضافة عبر محاورة تخصيص
  اختصارات البرنامج, من فئة أدوات.

## مستجدات الإصدار 1.0 ##

* إصدار أولي
* ترجمة الإضافة إلى اللغة الفرنسية

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=ubi
