# Unicode Braille Girişi

* Yazarlar: Mesar Hameed, Patrick Zajda, Leonard de Ruijter.
* [kararlı sürümü indir][1]

Bu eklenti, birkaç Braille dönüştürme görevi gerçekleştirmenize olanak tanır.
Örneğin, Braille nokta gösterimindeki metni (Örn. 1345-1236-145-1) Unicode veya ASCII Braille karakterlerine dönüştürebilirsiniz.
Metni, yazma alanına yazarak, yapıştırarak ya da bir metin dosyasını içe aktararak, seçili girdi veya çıktı braille tablosuna göre dönüştürebilirsiniz.
Sonuç panoya kopyalanabilir, bir metin veya BRF dosyasına aktarılabilir.

Bu özel eklentinin ilk amacı, liblouis tablolarını geliştirmeye yardımcı olmayı ve diliniz için otomatik testler eklemeyi kolaylaştırmaktı.
Ancak, NVDA 2017.3'te unicode braille tablosunun eklenmesiyle, bu eklenti artık bunun için gerekli değildir.
Kullanıcılar artık Braille klavye veya [PC Klavye ile Braille Girişi eklentisi][2] aracılığıyla bu tabloyla Braille girmeyi seçebilirler.

## Kullanım örneği

* Bir metin düzenleyicisi açın (örneğin Notepad Plus Plus).

* NVDA+Ctrl+i tuşlarına basın veya NVDA araçlar menüsünde bulunan Unicode Braille Girişi'ni seçin.

* Braille metninizi sırasıyla sayısal biçimde veya normal metninizde yazın. İsterseniz bir metin dosyasından da içe aktarabilirsiniz.

* Girişinizin braille noktalarından mı (ör. 1345-1236-145-1) yoksa mevcut braille tablosuna göre normal metinden mi (ör. Felemenkçe (Hollanda)) oluştuğunu seçin.

* Çıktı türünü seçin. Unicode braille'e bırakın veya isterseniz BRF veya NABC olarak değiştirin.

* Dışa aktarma türünü seçin:
  * `Pano` olarak ayarlandığında, sonuç panonuza kopyalanır ve  Tamam düğmesine bastıktan sonra yapıştırmaya hazır hale gelir.
  * "Dosya" olarak ayarlandığında, Tamam'a bastıktan sonra bir kaydetme penceresi görünecektir.

## Değişiklikler

### 5.0 için değişiklikler

* Eklenti artık NVDA 2024.3 veya daha yenisini gerektiriyor
* Radyo düğmeleri açılır liste kutularına dönüştürüldü
* ASCII braille (BRF) ve NABC (tam Latin1 karakter setine sahip Kuzey Amerika Braille Bilgisayar Kodu) için çıktı türleri eklendi

### 4.1 için değişiklikler

* Eklenti artık NVDA 2023.1 veya daha yenisini gerektiriyor
* Girdi tablosu olarak özel braille tabloları için destek eklendi

### 4.0 için değişiklikler

* Eklenti NVDA 2024.1 ile uyumlu
* Unicode Braille iletişim kutusunu açma hareketi NVDA+kontrol+U'dan NVDA+kontrol+i'ye değiştirildi

### 3.4 için değişiklikler

* Eklenti NVDA 2023.1 ile uyumlu

### 3.3 için değişiklikler

* Eklenti NVDA 2022.1 ile uyumlu

### 3.2 için değişiklikler

* Eklenti NVDA 2021.1 ile uyumlu
* Nokta giriş modunda yanlış giriş sağlandığında geri izlemeye neden olan bir sorun düzeltildi. Artık bunun yerine kolay bir mesaj kutusu gösteriliyor
* Çeviriler güncellendi.

### 3.1 için değişiklikler

* Radyo düğmeleri ve girdi düzenleme kontrolü için sekme sırası değiştirildi.
* Çeviriler güncellendi.

### 3.0 için değişiklikler

* Yeni bakıcı: Leonard de Ruijter.
* Eklenti, Python 3 ve dolayısıyla NVDA 2019.3 ve sonrası sürümler ile uyumlu.
* Seçili olan girdi braille tablosuna göre normal metinden unicode braille oluşturma yeteneği eklendi.

### 2.0 için değişiklikler

* Eklenti yardımına Eklenti Mağazasından ulaşılabilir.

### 1.1 için değişiklikler

* Seslendirilenlerin doğru şekilde duyulmasını sağlamak için gecikme süresi iyileştirildi.
* Birçok yeni çeviri.
* NVDA yardım menüsü altında Yardım belgesi eklendi.
* Boş braille'i (karakter 0x2800) isteğe bağlı olarak normal aralık karakteriyle değiştirmek için bir onay kutusu eklendi.
* Kısayollar artık Tercihler kategorisi altındaki Girdi Hareketleri iletişim kutusu kullanılarak yeniden atanabilir.

### 1.0 için değişiklikler

* İlk sürüm
* Yeni Diller: Fransızca

[1]: http://addons.nvda-project.org/files/get.php?file=ubi

[2]: https://github.com/nvdaes/pcKbBrl
