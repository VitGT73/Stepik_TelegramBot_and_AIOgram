from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import config

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = config.BOT_TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые ваши картинки,
async def send_photo_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_photo(message.photo[0].file_id)


# Этот хендлер обрабатывает Стикеры
async def send_sticker_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_sticker(message.sticker.file_id)


async def send_animation_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_animation(message.animation.file_id)


# Этот хэндлер будет срабатывать на любые ваши аудио файлы,
# !!!!!!!!!!!!!!
async def send_audio_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply_audio(message.audio.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.reply(text=message.text)


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_animation_echo, F.animation)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
