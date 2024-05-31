#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    
    keyboard = [
        [InlineKeyboardButton("🕹 Play & Earn MONEY ",url="https://t.me/theYescoin_bot/Yescoin?startapp=OuwKOg")],
        [
            InlineKeyboardButton("🐦Twitter",url="https://x.com/yescoin_fam"),
            InlineKeyboardButton("📣Channel",url="https://t.me/theYescoin"),
        ],
        [
            InlineKeyboardButton("Chat 1",url="https://t.me/theYescoin_fam2"),
            InlineKeyboardButton("Chat 2",url="https://t.me/theYescoin_EN"),
            InlineKeyboardButton("Chat 3",url="https://t.me/theyescoin_fam"),
        ],
        [
            InlineKeyboardButton("Chat 4",url="https://t.me/Official_Yescoin"),
            InlineKeyboardButton("Chat 5",url="https://t.me/Yescoin_fam2"),
            InlineKeyboardButton("Chat 6",url="https://t.me/realYescoin_global"),
        ],
        [
            InlineKeyboardButton("Chat 7",url="https://t.me/theYescoin_chat2"),
            InlineKeyboardButton("Chat 8",url="https://t.me/theYescoin_global2"),
            InlineKeyboardButton("Chat 9",url="https://t.me/theYescoin_chat9"),
        ],
        [
            InlineKeyboardButton("Chat 10",url="https://t.me/theYescoin_chat10"),
            InlineKeyboardButton("Chat 11",url="https://t.me/theYescoin_chat11"),
            InlineKeyboardButton("Chat 12",url="https://t.me/theYescoin_chat12"),
        ],
        [
            InlineKeyboardButton("Chat 13",url="https://t.me/realYescoin_chat1"),
            InlineKeyboardButton("Chat 14",url="https://t.me/theYescoinchat14"),
        ],
        [InlineKeyboardButton("🔒Private SALE", callback_data="Private SALE")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    txt=f"""
        Hi Yescoiner, <b>{str(update.message.from_user.username)} ！</b>

        Swipe finger and watch your balance grow. 
        Invite friends and get more coins together.

        Yescoin is what you want it to be.
        <b>LET 'S GO AND EARN MONEY</b> !
"""
    await update.message.reply_animation(animation="Lark20240416-123930.gif.mp4", caption=txt,reply_markup=reply_markup,parse_mode="HTML")
    

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query=update.callback_query

    txt=f"""
    Yescoin PRIVATE SALE
    $Yescoin Private Sale Price: 0.00003 USD
    $Yescoin Public Sale Price: 0.000069 USD

    If you buy Yescoin in the private sale with $30, you will receive 1,000,000 tokens. 
    At the public sale, your 1,000,000 tokens will be worth $69, giving you a 130%+ profit.

    To join the private sale, lets send  USDT to the wallet addresses below.

    Minimum purchase: $30 = 1,000,000 $Yescoin (Public Sale Price $69)
    Maximum purchase: $30,000 = 1,000,000,000 $Yescoin (Public Sale Price $69,000)


    Guaranteed profit of 130% at public launch


    We use cross-chain technology, so you can send using Solana/Ethereum/Binance Chain.


    USDT - TRC20
    TSphTT9AUZ4qH1rgLEd5Pw7vpGF7Hx3hRG  

    After you send USDT to the wallet above, please send your TON wallet address to this bot. 
    The bot will automatically send tokens equivalent to the amount of USD you sent.
"""
    inline_button=[[
        InlineKeyboardButton("Chat with Support",url="https://t.me/Master_ATK")
    ]]
    inline_markup= InlineKeyboardMarkup(inline_keyboard=inline_button)
    query = update.callback_query
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                    text=txt,reply_markup=inline_markup)


async def autosend(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6962487814:AAFIXch3QsAfKp16ECC33gn-7QRtAPyI6Xc").build()

    application.add_handlers([CommandHandler(["start","help"], start),
                              CallbackQueryHandler(button)]
                              )


    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()