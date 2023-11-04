from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
import wikipedia

BOT_TOKEN = '6517120796:AAGdHb6G7bUZ68RUc0r97C3aUjiCClA0Naw'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')

@dp.message_handler(commands=['start', ])
async def startfun(message: Message):
    await message.reply(f"Assalomu alaykum {message.from_user.full_name} Echo botga xush kelibsiz!!!")


@dp.message_handler(commands=['help', ])
async def helpfun(msg: Message):
    await msg.reply(f"Assalomu alaykum {msg.from_user.full_name} Sizga qanday yordam kerak!!!")

# @dp.message_handler()
# async def echofun(msg: Message):
#     await msg.reply(msg.text)


@dp.message_handler()
async def wikifun(msg: Message):
    try:
        respon = wikipedia.summary(msg.text)
        await msg.reply(respon)
    except:
        await msg.reply("Bunday maqola yoq")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
