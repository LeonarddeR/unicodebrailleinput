# UnicodeBrailleInput #

* Yazarlar: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* [kararlı sürümü indir][1]

Bu eklenti, metni braille'den (Örneğin: 1345-1236-145-1) Unicode braille
karakterlerine dönüştürmenizi sağlar. Metni, seçili olan giriş braille
tablosuna göre de dönüştürebilirsiniz.

Bu özel eklentinin amacı, liblouis tablolarının iyileştirilmesine yardımcı
olmayı ve diliniz için otomatik testler eklemeyi kolaylaştırmaktır. NVDA
2017.3'te unicode braille tablosunun eklenmesiyle, kullanıcılar yeni
tabloyla braille girmeyi seçebildikleri için bu eklenti artık bunun için
gerekli değildir. Ancak bu eklenti, normal metni belirli bir giriş tablosuna
göre unicode braille'e dönüştürmeye yine de yardımcı olabilir.

## Kullanım

* Unicode uyumlu bir metin düzenleyici açın (örneğin, Notepad++).
* NVDA+Ctrl+U tuşlarına basın veya NVDA araçlar menüsünde bulunan Unicode
  Braille Girişi'ni seçin.
* Girişinizin braille noktalarından mı (ör. 1345-1236-145-1) yoksa mevcut
  braille tablosuna göre normal metinden mi (ör. Felemenkçe (Hollanda))
  oluştuğunu seçin.
* Braille metninizi sırasıyla sayısal biçimde veya normal metninizle yazın.
* Tamam tuşuna basın.
* Gerekli unicode karakterler, yapıştırmanız için hazır olarak panonuza
  kopyalanacaktır.

## 3.0 için değişiklikler

* Yeni bakıcı: Leonard de Ruijter.
* Eklenti, Python 3 ve dolayısıyla NVDA 2019.3 ve üzeri ile uyumludur.
* Seçili olan giriş braille tablosuna göre normal metinden unicode braille
  oluşturma yeteneği eklendi.

## 2.0 için değişiklikler

* Eklenti yardımına Eklenti Yöneticisinden ulaşılabilir.

## 1.1 için değişiklikler ##

* Duyuruların doğru şekilde duyulmasını sağlamak için gecikme süresi
  iyileştirildi.
* Birçok yeni çeviri.
* NVDA yardım menüsü altında dokümantasyon eklendi.
* Boş braille'i (karakter 0x2800) isteğe bağlı olarak normal boşluk
  karakteriyle değiştirmek için bir onay kutusu eklendi.
* Kısayollar artık Tercihler kategorisi altındaki Girdi Hareketleri iletişim
  kutusu kullanılarak yeniden atanabilir.

## 1.0 için değişiklikler ##

* İlk sürüm
* Yeni Diller: Fransızca

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=unicodeBrailleInput
