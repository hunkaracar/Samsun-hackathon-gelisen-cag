def text_read(text):
    print("metin sifreleniyor...")
    print(text)
    metin=str(text['encrypted_text'])
    key=(str(text['key']))
    print(metin)
    print(key)
    decrypted_text=decrypt(metin,key)
    print(decrypted_text)
    return decrypted_text

def decrypt(encrypted_text,anahtar):
    import sympy as sp
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

    alfabe = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü','v','y','z']

    encrypted_values = []
    for char in encrypted_text:
        if char in alfabe:
            encrypted_values.append(alfabe.index(char))
    print("Şifrelenmiş metin karakterlerinin alfabe dizisindeki indeks numaraları:", encrypted_values)

    top_value = 0
    for char in anahtar:
        for key, value in x_anahtar.items():
            if value == char:
                top_value += key
                break
    top_value = top_value % 29
    print("Toplam değer (mod 29):", top_value)

    if len(encrypted_text) > len(anahtar):
        new_anahtar = anahtar
        fark = len(encrypted_text) - len(anahtar)
        for i in range(0, fark):
            new_anahtar = new_anahtar + anahtar[i]

        if top_value % 2 == 0:
            encrypted_text = encrypted_text[::-1]
        else:
            encrypted_text = encrypted_text[-1] + encrypted_text[1:-1] + encrypted_text[0]

        anahtar_key = []
        for i in new_anahtar:
            for key, value in x_anahtar.items():
                if value == i:
                    anahtar_key.append(key)

    elif len(encrypted_text) == len(anahtar):
        new_anahtar = anahtar
        if top_value % 2 == 0:
            encrypted_text = encrypted_text[::-1]
        else:
            encrypted_text = encrypted_text[-1] + encrypted_text[1:-1] + encrypted_text[0]
    else:
        print("Metin ve anahtar uzunlukları uyuşmuyor.")
        return
    
    anahtar_values = []
    for char in new_anahtar:
        for key, value in x_anahtar.items():
            if value == char:
                anahtar_values.append(key)
                break
    print("Anahtar değerlerin X koordinat düzlemindeki değerleri:", anahtar_values)

    try:

        encrypted_text_number = []
        for i in encrypted_text:
            if i in alfabe:
                encrypted_text_number.append(alfabe.index(i))
        print("Şifrelenmiş metin numaraları:", encrypted_text_number)

        decrypted_values = []
        for idx, val in enumerate(encrypted_text_number):
            key_val = anahtar_values[idx % len(anahtar_values)]
            step_value = (top_value + key_val) % 29
            mod_inverse = sp.mod_inverse(step_value, 29)
            decrypted_value = (mod_inverse * val) % 29
            decrypted_values.append(decrypted_value)
            print(f"Şifrelenmiş değer: {val}, Adım değeri: {step_value}, Modüler Ters: {mod_inverse}, Anahtar_düzmetin_değerleri: {decrypted_value}")
        
        decrypted_text = ''.join(alfabe[val] for val in decrypted_values)
        #print("Çözülen metin:", decrypted_text)

        decrypted_real_values = []
        for i in range(len(decrypted_values)):
            decrypted_real_value = (decrypted_values[i] - anahtar_values[i])
            decrypted_real_values.append(decrypted_real_value)

        print("Çözülen gerçek metin değerleri:", decrypted_real_values)

        decrypted_text = ''
        for value in decrypted_real_values:
            decrypted_text += y_metin.get(value, '')

        print("Deşifre edilmiş metin:", decrypted_text)
        return decrypted_text
    except Exception as e:
        print(e)

