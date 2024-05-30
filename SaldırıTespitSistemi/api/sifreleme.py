def text_read(text):
    print("metin sifreleniyor...")
    print(text)
    metin=str(text['text'])
    key=(str(text['key']))
    print(metin)
    print(key)
    sifreli_metin, anahtar=sifrele(metin,key)
    print(sifreli_metin,anahtar)
    return sifreli_metin,anahtar

def sifrele(text,key):
    y_metin = {
    -14: 'a', 
    -13: 'b', 
    -12: 'c',  
    -11: 'ç', 
    -10: 'd', 
    -9: 'e',
    -8: 'f',
    -7: 'g',  
    -6: 'ğ',
    -5: 'h',  
    -4: 'ı',  
    -3: 'i', 
    -2: 'j', 
    -1: 'k', 
     0: 'l', 
     1: 'm', 
     2: 'n', 
     3: 'o', 
     4: 'ö', 
     5: 'p', 
     6: 'r',  
     7: 's', 
     8: 'ş',  
     9: 't', 
     10: 'u',  
    11: 'ü', 
    12: 'v', 
    13: 'y', 
    14: 'z', 
}
    x_anahtar = { 
        14: 'a', 
        13: 'b', 
        12: 'c',  
        11: 'ç', 
        10: 'd', 
        9: 'e',
        8: 'f',
        7: 'g',  
        6: 'ğ',
        5: 'h',  
        4: 'ı',  
        3: 'i', 
        2: 'j', 
        1: 'k', 
        0: 'l', 
        -1: 'm', 
        -2: 'n', 
        -3: 'o', 
        -4: 'ö', 
        -5: 'p', 
        -6: 'r',  
        -7: 's', 
        -8: 'ş',  
        -9: 't', 
        -10: 'u',  
        -11: 'ü', 
        -12: 'v', 
        -13: 'y', 
        -14: 'z', 
    }
    alfabe = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']


    metin=text
    anahtar = key
    anahtar_top=0


    for i in anahtar:
        for key,value in x_anahtar.items():
            if value == i:
                anahtar_top = key + anahtar_top
                break
    anahtar_top_mod = anahtar_top % 29

    if len(metin) > len(anahtar):
        new_anahtar = anahtar
        fark = len(metin) - len(anahtar)
        for i in range(0,fark):
            new_anahtar = new_anahtar + anahtar[i]
    elif len(metin) == len(anahtar):
        new_anahtar = anahtar
    else:
        new_anahtar = anahtar
        fark = len(metin) - len(anahtar)
        new_anahtar = new_anahtar[:-2]

    m1 = []
    a1 = []
    t1 = []  #  a1 + m1
    c2 = []  # 10 + 11 , 10 + -4
    c3 = [] #mod almadan önceki hali

    for i in new_anahtar:
        for key,value in x_anahtar.items():
            if value == i:
                a1.append(key)
                
                
    for i in metin:
        for key,value in y_metin.items():
            if value == i:
                m1.append(key)
                break

    c2 = [0] * len(a1)

    for i in range(len(a1)):
        c2[i] = a1[i] + anahtar_top_mod

    t1 = [a + c for a, c in zip(a1, m1)]

    c3 = [(a * c) % 29 for a, c in zip(t1, c2)]


    encrypted_text = ' '
    for i in c3:
        encrypted_text += alfabe[i]

    # en son
    if (anahtar_top % 29) % 2 == 0:
        print("anahtar çift sayıdır")
        encrypted_text = encrypted_text[::-1]
    else:
        print("anahtar tek sayıdır")
        encrypted_text =  encrypted_text[-1] + encrypted_text[1:-1] + encrypted_text[0]

    return encrypted_text,anahtar
