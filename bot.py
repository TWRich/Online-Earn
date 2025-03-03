from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# Get bot token from environment variable
BOT_TOKEN = os.getenv("8112735504:AAHfM_HfvkGWyPBiyoWK1cD-FrQgETKMEtA")

# List of money-making ideas
money_methods = {
    "Freelancing": "You can earn money by offering skills on Upwork, Fiverr, and Freelancer.",
    "Affiliate Marketing": "Earn commissions by promoting products on Amazon Associates, ClickBank, or ShareASale.",
    "Online Courses": "Sell courses on Udemy or Teachable if you have expertise in a topic.",
    "Blogging": "Create a blog and monetize with Google AdSense or affiliate links.",
    "YouTube": "Start a YouTube channel and earn from ads, sponsorships, or memberships.",
    "Dropshipping": "Start an online store without holding inventory using Shopify and AliExpress.",
    "Stock Trading": "Invest in stocks or cryptocurrency for long-term gains."
}

# Start command
def start(update: Update, context: CallbackContext):
    reply_keyboard = [[method] for method in money_methods.keys()]
    update.message.reply_text(
        "Welcome! Choose a way to make money online:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

# Handle user selection
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    response = money_methods.get(text, "Please select a valid option.")
    update.message.reply_text(response)

# Main function
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
