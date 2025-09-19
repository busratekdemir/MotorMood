import os
import librosa
import numpy as np
import pandas as pd

# Dataset yolları
DATASET_DIR = "dataset"
CATEGORIES = ["agresif", "sakin"]

# Özellikleri tutacağımız liste
features = []

for category in CATEGORIES:
    folder = os.path.join(DATASET_DIR, category)
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)

        try:
            # Ses dosyasını yükle
            y, sr = librosa.load(file_path, sr=None)

            mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            mfccs_mean = np.mean(mfccs, axis=1)

            spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
            zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y))

            # Kaydet
            feature_dict = {
                "file": file_name,
                "label": category,
                "spectral_centroid": spectral_centroid,
                "zero_crossing_rate": zero_crossing_rate
            }

            # MFCC değerleri
            for i, mfcc in enumerate(mfccs_mean):
                feature_dict[f"mfcc_{i + 1}"] = mfcc

            features.append(feature_dict)

        except Exception as e:
            print(f"Hata: {file_path} dosyası işlenemedi. {e}")

# DataFrame'e çevir
df = pd.DataFrame(features)

# CSV olarak kaydet
df.to_csv("features.csv", index=False)

print("Özellik çıkarma tamamlandı ✅ features.csv oluşturuldu.")
