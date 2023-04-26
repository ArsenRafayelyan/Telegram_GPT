import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


token = '6240961893:AAETNkNiSIEZvhd_4hJ5Oi3kMQqi4rZIqTo'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message.text,
        temperature=0.7,
        max_tokens=60,
        n=1,
        stop=None,
        timeout=10
    )

    await message.answer(response.choices[0].text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
