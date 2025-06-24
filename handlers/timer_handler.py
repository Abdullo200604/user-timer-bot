import asyncio
import re
from telethon import events

def time_to_seconds(time_str):
    # Foydalanuvchi 1:10 yoki 01:10 yoki 00:01:10 kabi yozsa ham
    parts = list(map(int, time_str.strip().split(":")))
    while len(parts) < 3:
        parts = [0] + parts  # Har doim 3ta element: H, M, S

    h, m, s = parts
    return h * 3600 + m * 60 + s

def pretty_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    parts = []
    if h: parts.append(str(h))
    if h or m: parts.append(f"{m:02}" if h else str(m))
    parts.append(f"{s:02}" if (h or m) else str(s))
    return ":".join(parts)

def setup_handlers(client):
    # Ruxsat: .ok 11:11 yoki .ok 1:2:3 yoki .ok 00:01:11 kabi
    @client.on(events.NewMessage(pattern=r'\.ok ([\d:]+)'))
    async def timer_handler(event):
        time_str = event.pattern_match.group(1)
        total_seconds = time_to_seconds(time_str)

        for sec in range(total_seconds, 0, -1):
            await event.edit(f"⏳ {pretty_time(sec)}")
            await asyncio.sleep(1)
        await event.edit("✅ Timer tugadi!")
