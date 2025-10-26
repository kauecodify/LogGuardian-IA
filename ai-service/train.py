
# bibliotecas ------------------------------------------ #
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest
import pandas as pd, joblib, os
# ------------------------------------------------------ #

# criação do csv --------------------------------------- #
CSV_FILE = "sample_logs.csv"

if not os.path.exists(CSV_FILE):
    sample_logs = [
        "User admin logged in",
        "Database query executed",
        "Cache hit for key:user:123",
        "Failed password for root from 203.0.113.5",
        "rm -rf / --no-preserve-root",
        "Port scan from 185.130.5.231"
    ]
    pd.DataFrame({"log": sample_logs}).to_csv(CSV_FILE, index=False)
    print("sample_logs.csv criado!")
# ------------------------------------------------------ #

# leitura, transformação e vetorização do csv ---------- #
df = pd.read_csv(CSV_FILE)
vectorizer = TfidfVectorizer(max_features=100, stop_words="english")
X = vectorizer.fit_transform(df["log"])
# ------------------------------------------------------ #

# treinamento ------------------------------------------ #
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(X)
# ------------------------------------------------------ #

# save-------------------------------------------------- #
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("✅ Modelo e vetorizador treinados e salvos!")
# ------------------------------------------------------ #
