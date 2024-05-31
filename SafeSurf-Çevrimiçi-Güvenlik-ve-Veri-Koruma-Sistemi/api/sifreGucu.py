def text(girdi):
    return tahmin(girdi)

def tahmin(girdi):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.model_selection import train_test_split
    import numpy as np
    import pandas as pd
    import joblib

    model = joblib.load("C:/Users/Osman/Desktop/DOCUMENTS/Hackathon/app/models/SifreGücüBelirleme/sifregucu.pkl")
    data = pd.read_csv("C:/Users/Osman/Desktop/DOCUMENTS/Hackathon/app/models/SifreGücüBelirleme/data.csv",on_bad_lines="skip")
    data = data.head(130000)
    X = data['password']
    y = data['strengtha']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    girdi = str(girdi)
    dönüştürülmüş_girdi = vectorizer.transform([girdi])
    tahmin = model.predict(dönüştürülmüş_girdi)

    return tahmin
