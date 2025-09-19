import tkinter as tk
from tkinter import filedialog, messagebox
import librosa
import numpy as np
import joblib

model = joblib.load("motor_model.pkl")
encoder = joblib.load("label_encoder.pkl")

def select_file():
    file_path = filedialog.askopenfilename(
        title="Ses dosyası seç",
        filetypes=[("Ses dosyaları", "*.wav *.mp3 *.webm")]
    )
    if file_path:
        try:
            y, sr = librosa.load(file_path, sr=None)
            mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            mfccs_mean = np.mean(mfccs, axis=1)
            spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
            zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y))
            features = [spectral_centroid, zero_crossing_rate] + list(mfccs_mean)
            prediction = model.predict([features])[0]
            label = encoder.inverse_transform([prediction])[0]
            messagebox.showinfo("Sonuç", f"🎯 Tahmin: {label}")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya işlenemedi: {e}")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("MotorMood 🚀")
root.geometry("350x200")

label = tk.Label(root, text="MotorMood - Sürüş Tarzı Analizi", font=("Arial", 12))
label.pack(pady=20)

btn = tk.Button(root, text="Ses Dosyası Seç ve Analiz Et", command=select_file, width=30)
btn.pack(pady=10)

exit_btn = tk.Button(root, text="Çıkış", command=exit_app, width=30, bg="red", fg="white")
exit_btn.pack(pady=10)

root.mainloop()
