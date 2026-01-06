from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import os

# Telegram bot tokeni (Railway’da qo‘shiladi)
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Asosiy menyu
def main_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("📚 Maktab testlari (5–11)", callback_data="school"),
        InlineKeyboardButton("🎓 Abituriyent testi", callback_data="abituriyent"),
        InlineKeyboardButton("📊 Natijalarim", callback_data="results"),
        InlineKeyboardButton("💎 Premium", callback_data="premium"),
        InlineKeyboardButton("🍩 Donat rivojimiz uchun", callback_data="donate")
    )
    return keyboard

# /start buyrug‘i
@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer(
        "👋 Assalomu alaykum!\n"
        "FanTest botiga xush kelibsiz.\n\n"
        "Quyidagilardan birini tanlang:",
        reply_markup=main_menu()
    )

# Tugmalar bosilganda
@dp.callback_query_handler(lambda c: True)
async def buttons(call: types.CallbackQuery):
    await call.answer()

    if call.data == "school":
        await call.message.answer("📚 Maktab testlari tez orada ishga tushadi.")
    elif call.data == "abituriyent":
        await call.message.answer("🎓 Abituriyent testi tez orada ishga tushadi.")
    elif call.data == "results":
        await call.message.answer("📊 Natijalar hali yo‘q.")
    elif call.data == "premium":
        await call.message.answer("💎 Premium: Kunlik / Oylik / Yillik")
    elif call.data == "donate":
        await call.message.answer("🍩 Donat qilish uchun karta/Payme/Click qo‘shiladi.")

# Botni ishga tushirish
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
