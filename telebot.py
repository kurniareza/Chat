from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Masukkan token bot Telegram Anda di sini
TOKEN = "7602563074:AAF5ulDgNi7EPdI6ZBynxoEAbCVErnXVlS4"

# Fungsi untuk menangani perintah /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Halo! Iam ChatRichpt....")

# Fungsi untuk menangani perintah /help
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Gunakan perintah berikut:\n/start - Mulai bot\n/help - Bantuan")

# Fungsi utama untuk menjalankan bot
def main():
    print("🚀 Bot sedang berjalan... Tekan Ctrl + C untuk berhenti.")

    # Gunakan `Application.builder()`
    app = Application.builder().token(TOKEN).build()

    # Tambahkan handler untuk perintah
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Jalankan bot
    app.run_polling()

if __name__ == '__main__':
    main()