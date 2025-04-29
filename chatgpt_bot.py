import openai
import telebot

# 🔐 API калитларингизни бу ерга қўйинг
openai.api_key = "OPENAI_API_KEYINGIZNI_BU_YERGA_QOYING"
bot = telebot.TeleBot("TELEGRAM_BOT_TOKENINGIZNI_BU_YERGA_QOYING")

# 💬 Ҳар қандай хабарни қабул қилиш
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Агар сизда GPT-4 API бор бўлса, шуни ёзинг
            messages=[{"role": "user", "content": message.text}]
        )
        reply = response['choices'][0]['message']['content']
        bot.send_message(message.chat.id, reply)
    except Exception as e:
        bot.send_message(message.chat.id, "Хатолик юз берди: " + str(e))

# ▶️ Ботни ишга тушириш
print("🤖 Бот ишга тушди!")
bot.polling()
