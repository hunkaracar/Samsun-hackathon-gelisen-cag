Elbette, işte tüm içeriği tek bir `README.md` dosyası olarak hazırladım:

```markdown
# Saldırı Tespit Sistemi

Bu proje, kullanıcıdan alınan URL veya IP adresine yönelik saldırı olup olmadığını tespit eden bir React uygulamasıdır. Uygulama, girilen adresi analiz eder ve olası saldırı türünü belirler.

## Özellikler

- Kullanıcı dostu arayüz
- URL veya IP adresi girişi
- Analiz sonuçlarını görüntüleme
- Yükleniyor animasyonu

## Kurulum

Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin.

### Gerekli Yazılımlar

- Node.js (>= 14.x)
- npm veya yarn paket yöneticisi

### Adımlar

1. Bu projeyi klonlayın veya indirin:
   ```bash
   git clone https://github.com/kullaniciadi/saldiri-tespit-sistemi.git
   cd saldiri-tespit-sistemi
   ```

2. Gerekli bağımlılıkları yükleyin:
   ```bash
   npm install
   # veya
   yarn install
   ```

3. Uygulamayı çalıştırın:
   ```bash
   npm start
   # veya
   yarn start
   ```

4. Tarayıcınızda `http://localhost:3000` adresine giderek uygulamayı görüntüleyin.

## Kullanım

1. Uygulamayı başlattıktan sonra, URL veya IP adresini giriş alanına yazın.
2. `Analiz Et` butonuna tıklayın.
3. Analiz sonuçlarını ve saldırı türünü ekranın altında görüntüleyin.

## API

Bu uygulama, arka planda çalışan bir API'yi kullanır. API, girilen URL veya IP adresine yönelik saldırı olup olmadığını tespit eder ve sonuçları JSON formatında döner.

### API İstekleri

- **POST** `/api/sts`
  - **Girdi:** `{ "url_or_ip": "girilmis_url_veya_ip" }`
  - **Çıktı:** `{ "attack_type": "saldiri_turu" }`

### Örnek İstek

```bash
curl -X POST http://127.0.0.1:5000/api/sts -H "Content-Type: application/json" -d '{"url_or_ip": "example.com"}'
```

## Proje Yapısı

```plaintext
saldiri-tespit-sistemi/
├── public/
│   ├── index.html
│   └── ...
├── src/
│   ├── App.js
│   ├── index.js
│   └── Sts.js
├── package.json
├── README.md
└── ...
```

- `public/`: Statik dosyalar ve ana HTML dosyası.
- `src/`: React bileşenleri ve ana uygulama dosyaları.
- `App.js`: Ana uygulama bileşeni.
- `index.js`: Uygulamanın giriş noktası.
- `Sts.js`: Saldırı Tespit Sistemi bileşeni.

## Katkıda Bulunma

Katkılarınızı memnuniyetle kabul ediyoruz! Lütfen önce bir konu açarak değişikliklerinizi tartışın.

1. Fork yapın (https://github.com/kullaniciadi/saldiri-tespit-sistemi/fork)
2. Bir dal oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi yapın (`git commit -m 'Add some AmazingFeature'`)
4. Dalınıza ittirin (`git push origin feature/AmazingFeature`)
5. Bir Pull Request açın

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - daha fazla bilgi için `LICENSE` dosyasına bakın.

## Kullanılan Teknolojiler

- React
- Node.js
- npm veya yarn
- Flask (API için)

## Ekran Görüntüleri

Ana ekran:
![Ana Ekran](screenshots/main_screen.png)

Analiz Sonuçları:
![Analiz Sonuçları](screenshots/results.png)

## Yazarlar

- **İsim Soyisim** - *İlk çalışma* - [Kullanıcı Adı](https://github.com/kullaniciadi)

## Teşekkür

Bu projede katkısı olan herkese teşekkürler!

```

Bu dosyayı `README.md` adıyla projenizin kök dizinine kaydedebilirsiniz.