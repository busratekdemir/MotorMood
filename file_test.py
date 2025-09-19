import librosa
import numpy as np
import joblib

# Modeli ve encoder'ı yükle
model = joblib.load("motor_model.pkl")
encoder = joblib.load("label_encoder.pkl")   # ✅ label'ı da kaydetmemiz lazım

# Test dosyası
test_file = "dataset/agresif/agresif5.wav"

y, sr = librosa.load(test_file, sr=None)

mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
mfccs_mean = np.mean(mfccs, axis=1)
spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y))

features = [spectral_centroid, zero_crossing_rate] + list(mfccs_mean)

prediction = model.predict([features])[0]

# Encoder ile geri çevir
label = encoder.inverse_transform([prediction])[0]

print("🎯 Tahmin:", label)
