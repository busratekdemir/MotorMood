# MotorMood 🚀

Motor sesinden sürüş tarzı analizi (Agresif / Sakin)  
Driving style analysis from motorcycle sound (Aggressive / Calm)

## 📌 Açıklama
TR: Python ile geliştirilmiş, ses dosyalarını işleyip makine öğrenmesi ile sınıflandırma yapan uygulama.  
EN: A Python-based application that processes audio files and classifies riding style using machine learning.

## 📂 Proje Yapısı
- `dataset/` → Ses verileri
- `feature_extraction.py` → Ses dosyalarından özellik çıkarır
- `train_model.py` → Modeli eğitir
- `file_test.py` → Tek dosya üzerinden test yapar
- `app.py` → Tkinter arayüzü (ses seç → analiz → sonuç)
- `requirements.txt` → Gerekli kütüphaneler

## 🚀 Çalıştırma
```bash
git clone https://github.com/kullaniciadi/MotorMood.git
cd MotorMood
pip install -r requirements.txt
python app.py
