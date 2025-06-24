from telethon import TelegramClient
from config import API_ID, API_HASH, PHONE, SESSION_NAME
from handlers.timer_handler import setup_handlers

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    print("⏳ Userbot tayyorlanmoqda...")
    await client.start(phone=PHONE)

    # 👇 Bu yerda user haqida ma'lumot chiqaramiz
    print("✅ Kirildi! Endi foydalanuvchi ma'lumotlari olinmoqda...\n")
    me = await client.get_me()
    print(f"👤 Username: {me.username}")
    print(f"🆔 ID: {me.id}")
    print(f"📞 Phone: {me.phone}")
    print(f"💬 Full name: {me.first_name} {me.last_name or ''}")

    # Handlerlarni o‘rnatamiz
    setup_handlers(client)
    print("♻️  Bot tayyor! Chatda .ok 00:00:10 deb yozib test qilib ko‘ring.")
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
