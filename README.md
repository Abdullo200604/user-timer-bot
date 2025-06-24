# ⏳ user-timer-bot

Telegram foydalanuvchi bot — vaqtni ortga sanaydigan kuchli **User Timer Bot** (Telethon asosida)!

## 🚀 Qanday ishlaydi?

- Telegramda istalgan chatda `.ok 01:23:45` yoki `.ok 90:00` kabi yozing
- Xabar **ortga qarab** har soniyada tahrirlanadi (timer)
- Eng qisqa, boshida 0 bo‘lmagan ko‘rinishda chiqadi (`59:05`, `1:01:10`, `10` va h.k.)

## 🔥 Namuna:

.ok 1:10

Copy
Edit
👉  
⏳ 1:10
⏳ 1:09
...
⏳ 0:01
✅ Timer tugadi!

less
Copy
Edit

## 🛠 O‘rnatish

1. Telegram developer portalidan `API_ID` va `API_HASH` oling: [my.telegram.org](https://my.telegram.org)
2. `.env` faylga quyidagilarni yozing:
    ```
    API_ID=YOUR_API_ID
    API_HASH=YOUR_API_HASH
    PHONE=+998YYXXXXXXX
    SESSION_NAME=user_session
    ```
3. Zarur paketlarni o‘rnating:
    ```bash
    pip install telethon python-dotenv
    ```
4. Botni ishga tushiring:
    ```bash
    python main.py
    ```
    Birinchi marta SMS va (bo‘lsa) 2FA so‘raydi. Keyingi safar avtomatik ulanadi.

## 📂 Tuzilma

user-timer-bot/
├─ handlers/
│ └─ timer_handler.py
├─ main.py
├─ config.py
├─ .env
├─ .gitignore
└─ README.md

less
Copy
Edit

## 📦 Texnologiyalar

- **Python 3.8+**
- [Telethon](https://github.com/LonamiWebs/Telethon)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

## ✨ G‘oya va kreativlik
- Barcha vaqt formatlarini qo‘llaydi: `ss`, `mm:ss`, `hh:mm:ss`
- Xabarni har doim eng chiroyli va qisqa formatda ko‘rsatadi

## 👨‍💻 Muallif

[@Mr_FoxDev](https://github.com/Abdullo200604)

---

**Yordam yoki xatolik bo‘lsa, Issue qoldiring!**