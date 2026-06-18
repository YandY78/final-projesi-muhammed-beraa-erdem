# Akademik Yapay Zeka Asistanı

## Proje Adı

Akademik Yapay Zeka Asistanı

## Problem Tanımı

Öğrenciler ve kullanıcılar ders notları, dokümanlar ve kaynaklar içerisinde bilgi ararken zaman kaybetmektedir. Bu proje, kaynak dosyalar içerisindeki bilgilere daha hızlı erişim sağlamak amacıyla geliştirilmiştir.

## Hedef Kullanıcı

* Üniversite öğrencileri
* Eğitim materyalleri kullanan kişiler
* Akademik içeriklerle çalışan kullanıcılar

## Çözümün Kısa Açıklaması

Akademik Yapay Zeka Asistanı, kullanıcının sorduğu sorulara kaynak dosyaları tarayarak cevap veren masaüstü bir uygulamadır. Sistem ilgili bilgiyi bulduğunda cevabı ve kullanılan kaynak dosyasını kullanıcıya göstermektedir.

## Kullanılan Teknolojiler

* Python
* Tkinter
* Git
* GitHub

## Veri Kaynakları

Proje kapsamında örnek veri kaynakları olarak data klasörü altında bulunan TXT dosyaları kullanılmaktadır.

* kaynak1.txt
* kaynak2.txt
* kaynak3.txt
* kaynak4.txt
* kaynak5.txt

## Sistem Mimarisi / İş Akışı

1. Kullanıcı uygulamayı başlatır.
2. Soru giriş alanına soru yazar.
3. Sor butonuna basar.
4. Sistem data klasöründeki kaynak dosyalarını tarar.
5. İlgili bilgi bulunursa cevap ekranda gösterilir.
6. Cevap ile birlikte kullanılan kaynak dosyası görüntülenir.

## Kurulum Adımları

1. Projeyi GitHub üzerinden indiriniz.
2. Bilgisayarınızda Python kurulu olduğundan emin olunuz.
3. Proje klasörünü açınız.
4. Terminal üzerinden aşağıdaki komutu çalıştırınız:

python main.py

## Kullanım Biçimi

1. Programı çalıştırın.
2. Soru kutusuna sorunuzu yazın.
3. Sor butonuna basın.
4. Sistem cevabı ve kaynak bilgisini gösterecektir.

## Yapay Zeka Araçları

Bu proje geliştirilirken aşağıdaki yapay zeka araçlarından yararlanılmıştır:

* ChatGPT
* Google Gemini

Bu araçlar kod geliştirme, dokümantasyon oluşturma ve hata ayıklama süreçlerinde destek amaçlı kullanılmıştır.

## Kullanım Senaryosu

Örnek:

Soru:
RAG nedir?

Sonuç:
Kaynak: kaynak2.txt

RAG, Retrieval Augmented Generation anlamına gelir. Önce kaynaklardan bilgi aranır. Daha sonra yapay zeka bu bilgileri kullanarak cevap üretir.

## Örnek Ekran Görüntüleri

Uygulamanın çalışır durumdaki ekran görüntüleri proje deposunda paylaşılmıştır.

## Test Sonuçları

### Başarılı Testler

Soru:

* RAG nedir?
* SHAP nedir?

Sonuç:

* Sistem ilgili kaynağı bulup cevap göstermiştir.

### Başarısız Testler

Soru:

* Türkiye'nin başkenti nedir?
* Python'u kim geliştirdi?

Sonuç:

* Kaynak dosyalarında ilgili bilgi bulunamadığından sistem cevap üretememiştir.

## Bilinen Eksiklikler

* Sistem yalnızca kaynak dosyalarında bulunan bilgileri kullanmaktadır.
* PDF desteği henüz eklenmemiştir.
* Gelişmiş yapay zeka modeli entegrasyonu bulunmamaktadır.
* Arama mekanizması anahtar kelime temellidir.

## Sürüm Bilgisi

Final sürümü GitHub üzerinde v1.0.0 etiketi ile yayımlanmıştır.

## Geliştirici

Muhammed Beraa Erdem

Öğrenci No: 2544001021
