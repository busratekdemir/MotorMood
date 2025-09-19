import os
from moviepy.editor import AudioFileClip

# Klasörleri otomatik oluştur
os.makedirs("dataset/agresif", exist_ok=True)
os.makedirs("dataset/sakin", exist_ok=True)

# Orijinal indirilmiş dosya
input_file = "motor7.webm"

clip = AudioFileClip(input_file)

while True:
    print("\n=== Yeni Ses Kırpma İşlemi ===")

    kategori = input("Kategori (agresif/sakin, çıkmak için q): ").strip().lower()
    if kategori == "q":
        print("Çıkılıyor...")
        break
    if kategori not in ["agresif", "sakin"]:
        print("Hatalı kategori! 'agresif' veya 'sakin' yaz.")
        continue

    try:
        start_time = int(input("Başlangıç (saniye): "))
        end_time = int(input("Bitiş (saniye): "))
    except ValueError:
        print("Sadece sayı gir!")
        continue

    # Dosya numarasını belirle
    existing_files = os.listdir(f"dataset/{kategori}")
    dosya_no = len(existing_files) + 1
    output_file = f"dataset/{kategori}/{kategori}{dosya_no}.wav"

    # Kırpma işlemi
    part = clip.subclip(start_time, end_time)
    part.write_audiofile(output_file)

    print(f"Kırpma tamam ✅ {output_file}")
