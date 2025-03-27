#Добавить игру, реализованную ранее, с конфетами к боту.
#Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга.
#Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

import logging
import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, ConversationHandler

# Включаем логгирование ошибок
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)

CANDIES, TURN, GAME_OVER = range(3)

def start(update: Update, context: CallbackContext) -> int:
    """Начало игры"""
    update.message.reply_text("Добро пожаловать в игру Candy Game! 🍬🎮")
    update.message.reply_text("На столе лежит 117 конфет. Каждый игрок за ход может взять от 1 до 28 конфет.\n"
                             "Тот, кто заберет последнюю конфету, проиграет. Первый ход определяется жребием.")
    update.message.reply_text("Начнём игру? Нажмите /play для начала.")
    return CANDIES

def play_game(update: Update, context: CallbackContext) -> int:
    """Запуск игры"""
    candies = 117  # начальное количество конфет
    players = ['Человек', 'Бот']
    first_turn = random.choice([0, 1])  # выбор первого хода
    current_turn = first_turn  # Текущий игрок
    context.user_data['candies'] = candies
    context.user_data['players'] = players
    context.user_data['first_turn'] = first_turn
    context.user_data['current_turn'] = current_turn
    update.message.reply_text(f"На столе {candies} конфет. Первым ходит {players[current_turn]}.")
    return TURN

def make_turn(update: Update, context: CallbackContext) -> int:
    """Выполнение хода игроком"""
    players = context.user_data['players']
    current_turn = context.user_data['current_turn']
    candies = context.user_data['candies']

    if current_turn == 0:  # Ход человека
        try:
            take = int(update.message.text)
            if take < 1 or take > 28:
                raise ValueError
            if take > candies:
                raise ValueError
            candies -= take
            context.user_data['candies'] = candies
            if candies == 0:
                update.message.reply_text(f"Вы взяли {take} конфет. Осталось 0 конфет. Вы проиграли 😢")
                return GAME_OVER
            else:
                update.message.reply_text(f"Вы взяли {take} конфет. Осталось {candies} конфет.")
                current_turn = 1  # Следующий ход бота
                context.user_data['current_turn'] = current_turn
                bot_turn = random.randint(1, min(28, candies))
                candies -= bot_turn
                context.user_data['candies'] = candies
                update.message.reply_text(f"Бот взял {bot_turn} конфет. Осталось {candies} конфет.")
                if candies == 0:
                    update.message.reply_text(f"Бот забрал последние конфеты. Вы победили! 🎉")
                    return GAME_OVER
                else:
                    update.message.reply_text(f"Теперь ваш ход. Сколько конфет хотите взять?")
                    return TURN
        except ValueError:
            update.message.reply_text("Неверное количество конфет. Выберите от 1 до 28, но не больше оставшихся.")
            return TURN
    else:  # Ход бота
        bot_turn = random.randint(1, min(28, candies))
        candies -= bot_turn
        context.user_data['candies'] = candies
        update.message.reply_text(f"Бот взял {bot_turn} конфет. Осталось {candies} конфет.")
        if candies == 0:
            update.message.reply_text(f"Бот забрал последние конфеты. Вы победили! 🎉")
            return GAME_OVER
        else:
            update.message.reply_text(f"Теперь ваш ход. Сколько конфет хотите взять?")
            current_turn = 0  # Следующий ход человека
            context.user_data['current_turn'] = current_turn
            return TURN

def cancel(update: Update, context: CallbackContext) -> int:
    """Завершить игру"""
    update.message.reply_text("Игра закончена. До встречи!")
    return ConversationHandler.END

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CANDIES: [MessageHandler(Filters.regex('^(/play)$'), play_game)],
            TURN: [MessageHandler(Filters.text & ~Filters.command, make_turn)],
            GAME_OVER: [MessageHandler(Filters.all, cancel)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    