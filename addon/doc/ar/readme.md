# UnicodeBrailleInput #

* مطورو الإضافة: Mesar Hameed, Patrick Zajda.
* download [stable version][1]
* download [development version][2]

تتيح لك هذه الإضافة تحويل النص من برايل (على سبيل المثال,
1345-1236-145-1)إلى أحرف بشفرة برايل الموحدة.

الغرض من هذه الإضافة هو سهولة المساهمة في تطوير وتحسين جداول ليبلويس كما
أنها تمكن من الاختبار الآلي للخط البارز بلغتك.

## الاستخدام ##

* قم بفتح محرر نصوص يسمح برؤية الشفرة الموحدة (unicode) كأن تفتح برنامج
  Notepad++, 
* Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools
  menu
* اكتب النص الذي تريد أن تختبره في صورة رقمية.
* اضغط زر موافق.
* سيتم نسخ الأحرف التي كتبتها في صورة رقمية بطريقة شفرة البرايل الموحدة مما
  يمكنك لصقها في أي مكان.

## Changes for 1.1-dev ##

* Improve delay to allow announcements to be heard correctly.
* Many new translations.
* Added documentation under NVDA help menu.
* Added a checkbox to optionally replace the space braille (character
  0x2800) by the regular space character.
* Shortcuts can now be reassigned using the NVDA gesture input dialog, under
  the Tools category.

## Changes for 1.0 ##

* Initial release
* New Languages: French

[[!tag dev stable]]

[1]: http://addons.nvda-project.org/files/get.php?file=ubi

[2]: http://addons.nvda-project.org/files/get.php?file=ubi-dev
