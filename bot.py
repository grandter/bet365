import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Get Bot Token from environment variable
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    welcome_text = (
        f"Hi {user.first_name}! 👋\n\n"
        "Welcome to **Win365**.\n"
        "Your sports companion for match updates, live scores, fixtures and the latest sports news.\n\n"
        "Send /help to see available commands."
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = (
        "**Available Commands:**\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/status - Check if the bot is online\n\n"
        "I am ready to assist you with quick sports updates!"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Quick online check"""
    await update.message.reply_text("✅ Win365 is active and ready!")

def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set.")

    # Create Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status))

    # Start bot (long polling)
    logging.info("Win365 bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
