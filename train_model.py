import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. CSV'yi oku
df = pd.read_csv("features.csv")

# 2. Özellikler ve etiketleri ayır
X = df.drop(columns=["file", "label"])   # sayısal özellikler
y = df["label"]                          # agresif / sakin

# 3. Etiketleri sayıya çevir (agresif=1, sakin=0 gibi)
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# 4. Eğitim / test ayırımı (%70 / %30)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 5. Logistic Regression modeli
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 6. Test verisinde tahmin
y_pred = model.predict(X_test)

# 7. Sonuçları yazdır
print("✅ Doğruluk Oranı (Accuracy):", accuracy_score(y_test, y_pred))
print("\n📊 Detaylı Rapor:\n", classification_report(y_test, y_pred, target_names=encoder.classes_))

joblib.dump(model, "motor_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")
print("💾 Model ve encoder kaydedildi.")