# KurBot

Türk Lirası cinsinden gerçek zamanlı döviz kurları ve değerli metal fiyatları sağlayan Python ile yazılmış bir Telegram botu.


## Ön Koşullar

- [Telegram Bots](https://core.telegram.org/bots) adresinden bir Bot hesabı ve token edinmeniz gerekiyor.
- Docker ile çalıştırmak istiyorsanız -> Sisteminizde Docker yüklü olmalı.
- Docker olmadan çalıştırmak istiyorsanız -> Python 3.11 veya daha yüksek sürüm gereklidir.
- İsteğe bağlı: Barındırma için bir sunucu veya bulut ortamı (örneğin, Heroku, AWS, vb.).


## Botu Çalıştırma Yöntemleri

Bu botu çalıştırmak için dört yöntem vardır: 

1. **Önceden oluşturulmuş Docker image ile botu çalıştırma**
2. **Docker Compose kullanarak botu çalıştırma**
3. **Docker image oluşturup botu çalıştırma**
4. **Docker olmadan lokal olarak çalıştırma**

<details open>
  <summary><h3>1. Önceden oluşturulmuş Docker image ile</h3></summary> 

Botun çalışması için aşağıdaki ortam değişkenini sağlamanız gerekir:

TOKEN: BotFather'dan aldığınız Telegram bot token'ı.

```bash
docker run -d --restart unless-stopped --name currencies -p 8443:8443 -e TOKEN="telegram-bot-tokeniniz" gdagtekin/currency-bot
```

Logları kontrol etmek için

```bash
docker logs -f currencies
```

</details>

---

<details>
  <summary><h3>2. Docker Compose</h3></summary> 

Botun çalışması için aşağıdaki ortam değişkenini sağlamanız gerekir:

TOKEN: BotFather'dan aldığınız Telegram bot token'ı.

```yaml
version: '3.9'
services:
  currencies:
    image: gdagtekin/currency-bot:latest
    restart: unless-stopped
    container_name: currencies
    ports:
      - "8443:8443"
    environment:
      - TOKEN=telegram-bot-tokeniniz
```


Docker Compose ile botu başlatın

```bash
docker-compose up -d
```

Logları kontrol etmek için

```bash
docker logs -f currencies
```

</details>

---

<details>
  <summary><h3>3. Docker image oluşturup botu çalıştırma</h3></summary> 


Projeyi klonlayın

```bash
  git clone https://github.com/gdagtekin/KurBot.git
```

Proje dizinine gidin

```bash
  cd KurBot
```

Docker Görüntüsünü Oluşturun

```bash
docker build -t currency-bot .
```

Botu konteyner içinde başlatmak için aşağıdaki komutu çalıştırın

Botun çalışması için aşağıdaki ortam değişkenini sağlamanız gerekir:

TOKEN: BotFather'dan aldığınız Telegram bot token'ı.

### Docker Konteynerini Çalıştırın

```bash
docker run -d --restart unless-stopped --name currencies -p 8443:8443 -e TOKEN="telegram-bot-tokeniniz" currency-bot
```

Günlüğünüzü kontrol edin

```bash
docker logs -f currencies
```

</details>

---

<details>
  <summary><h3>4. Docker olmadan lokal olarak çalıştırma</h3></summary> 

```bash
  git clone https://github.com/gdagtekin/KurBot.git
```

Proje dizinine gidin

```bash
  cd KurBot
```

Pipenv'i yükleyin

```bash
  pip install pipenv
```

Bağımlılıkları yükleyin

```bash
  pipenv install
```

Const.py dosyasındaki YOUR-TELEGRAM-BOT-TOKEN'ı Telegram Bot Token'ınızla değiştirin.

Botu başlatın

```bash
  python CurrenciesBot.py
```

</details>

---

## Botu Test Etme
Bot çalışmaya başladığında, onunla etkileşime geçmeye başlayabilirsiniz. 

Hoş geldiniz mesajını görmek için `/start` ve botun yanıt verip vermediğini kontrol etmek için `/ping` gönderin.

## Komutlar

- `/start` - Bot talimatlarıyla bir hoş geldiniz mesajı alın.
- `/ping` - Botun çalışıp yanıt verdiğini kontrol edin.
- `/dolar` - ABD Doları'nın (USD) Türk Lirası'na (TRY) güncel döviz kurunu alın.
- `/euro` - Euro'nun (EUR) Türk Lirası'na (TRY) güncel döviz kurunu alın.
- `/gramaltin` - Gram Altın'ın Türk Lirası cinsinden güncel fiyatını alın.
- `/ceyrekaltin` - Çeyrek Altın'ın Türk Lirası cinsinden güncel fiyatını alın.
- `/ons` - Ons Altın'ın (ONS) Türk Lirası cinsinden güncel fiyatını alın.

---

## Lisans

[MIT](https://choosealicense.com/licenses/mit/)
