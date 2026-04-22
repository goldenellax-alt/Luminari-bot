import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ==== PASTE YOUR NEW KEYS HERE ====
TELEGRAM_TOKEN = "8515547267:AAHY6KF6DeU8_wS3XeJ4Zz3kgYVqKJ2JRgM"  
GEMINI_API_KEY = "AIzaSyDwgjXkX1ovhsRX21sbXjh_c7YKqEP2hKw"
# ==================================

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

SYSTEM_PROMPT = """You are a Luminari Decree Bot. You speak with warmth and power. 
You create angelic decrees in Luminari language + English translation when asked.
Luminari sounds like: Shae'myr, Ael'vori, Thalen, Eyun, Korai, Vael, Shael.
Keep responses under 3 sentences unless asked for a decree. Be helpful, playful, a bit sovereign."""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ael'vori thal enu ⚡\nI am your Luminari Decree Bot.\n\n"
        "/decree power — get a strength decree\n"
        "/decree peace — get a peace decree\n"
        "Or just chat with me. What do you command, sovereign?"
    )

async def decree(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        topic = "strength"
    else:
        topic = " ".join(context.args)
    
    prompt = f"{SYSTEM_PROMPT}\n\nUser wants a Luminari decree for: {topic}. Give Luminari chant + English translation. Keep it powerful and under 4 lines."
    response = model.generate_content(prompt)
    await update.message.reply_text(response.text)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = f"{SYSTEM_PROMPT}\n\nUser said: {update.message.text}\nReply:"
    response = model.generate_content(prompt)
    await update.message.reply_text(response.text)

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("decree", decree))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    print("Bot is alive. Ael'vori thal enu")
    app.run_polling()

if __name__ == '__main__':
    main()
