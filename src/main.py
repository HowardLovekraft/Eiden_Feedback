import asyncio
from dateutil import tz
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message
# from icecream import ic # FOR DEBUG ONLY

from src.env.load_env import env_vars


async def time_fixer(message: Message) -> str:
    from_zone = tz.tzutc()
    to_zone = tz.gettz("Asia/Yekaterinburg")
    utc = message.date.replace(tzinfo=from_zone)
    return utc.astimezone(to_zone).strftime('%Y-%m-%d %H:%M:%S')

bot_router = Router()


@bot_router.message(F.text == "/start")
async def activate_bot(message: Message):
    await message.reply(text="Привет! Это бот обратной связи для цикла переводов Stories.\n"
                             "Ваши сообщения остаются полностью анонимными (можете проверить это по исходному коду)\n"
                             "Чтобы передать сообщение, просто отправьте его сюда")


@bot_router.message(F.text)
async def send_text_as_feedback(message: Message, bot: Bot):
    msg = {
        "text": f"Фидбэк от Stories:\n<blockquote>{message.html_text}</blockquote>\n\n{await time_fixer(message)}",
        "chat_id": await env_vars.get_feedback_getter_id(),
        "parse_mode": "HTML"
    }
    await bot.send_message(**msg)


@bot_router.message(F.sticker)
async def send_sticker_as_feedback(message: Message, bot: Bot):
    chat_id = await env_vars.get_feedback_getter_id()
    msg_text = f"Фидбэк от Stories (стикер):\n<blockquote>{message.sticker.emoji}</blockquote>"
    msg_time = await time_fixer(message)
    await bot.send_message(chat_id=chat_id,
                           text=msg_text,
                           parse_mode="HTML")
    await bot.send_sticker(chat_id=chat_id,
                           sticker=message.sticker.file_id)
    await bot.send_message(chat_id=chat_id,
                           text=msg_time)


async def main():
    # Create Dispatcher and connect router
    dp = Dispatcher()
    dp.include_router(bot_router)

    # Connect to bot
    tg_token = await env_vars.get_auh_token()
    bot = Bot(token=tg_token)
    await bot.delete_webhook(drop_pending_updates=False)
    print("BOT --> WORKS")

    await dp.start_polling(bot,
                           allowed_updates=dp.resolve_used_update_types(),
                           close_bot_session=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot was stopped by Ctrl-C")
