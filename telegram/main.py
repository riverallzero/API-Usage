from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

telegram_bot_token = 'telegram_token'
openai_api_key = 'openai_token'


def start(update):
    update.message.reply_text('Hi there, start conversation with ChatGPT')


def generate_response(user_input):
    openai.api_key = openai_api_key
    model = 'gpt-3.5-turbo'

    # Message
    messages = [
        {'role': 'user', 'content': f'{user_input}'},
    ]

    response = openai.ChatCompletion.create(model=model, messages=messages)
    answer = response['choices'][0]['message']['content']

    return answer


def reply(update):
    user_input = update.message.text
    response = generate_response(user_input)
    update.message.reply_text(response)


def main():
    bot_token = telegram_bot_token
    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
