def text(girdi):
    print(girdi)
    
    return tahmin(girdi)

def tahmin(girdi):
    import dill as pickle
    from utils import word  # word fonksiyonunu import ediyoruz

    # Modeli ve TF-IDF vektörleştiriciyi yükle
    with open("C:/Users/Osman/Desktop/DOCUMENTS/Hackathon/app/models/SifreGücüBelirleme/sifregucu.pkl", "rb") as f:
        model, tfidf = pickle.load(f)

    # Yeni kullanıcının şifresini tahmin et
    girdi = str(girdi)
    data = tfidf.transform([girdi])
    output = model.predict(data)
    print(output[0])
    output = str(output)
    return output

