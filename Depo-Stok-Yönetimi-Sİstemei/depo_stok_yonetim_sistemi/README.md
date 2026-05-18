# Proje 8: Depo ve Stok Yönetim Sistemi (PyQt5 + SQLite)

Bu proje, **PyQt5 masaustu arayuz** ve **SQLite** ile stok/urun yonetimi yapar.

## Ozellikler

- **Login + rol**: `admin` / `personel`
- **Kayit ol (personel)**: ad soyad + telefon + kullanici adi + sifre
- **CRUD**: Urunler ve Tedarikciler (admin yetkisi)
- **Stok giris/cikis/sayim**: hareket kaydi (audit log) ile
- **Dusuk stok uyarisi**: stok <= min stok
- **Rapor**: stok hareketleri listesi + arama
- **CSV disari aktarma**: gorunen stok hareketlerini CSV olarak kaydetme
- **Cikis (logout)**: uygulamayi kapatmadan tekrar giris ekranina doner

## Varsayilan kullanicilar

- **admin / admin123**
- **personel / 1234**

## Calistirma

```bash
pip install -r requirements.txt
python main.py
```
