from pyrogram import Client

from pyrogram import filters

import re

Account = "Account1"

api_id = 22206519

api_hash = "420b79542f3bae318a9a5e84951881a2"

session = "BABlxVKnxTg8cSKrRsW3JTffBP2ujzZYSlSmFaTfi5w1QMghRvl7MkicRCMMEJBiLCv5nXt1HFGTGd5Ag5wFFTeZuAjlYWCKunlgHDO33loQXLviMBU8kFDypjI8Nx1E0WLfbnCq_KQp6xY5Y0eY1lOksORGOoIF7Rw6YXeOuFIpQ_tH2NO7PbupqXS-SEjdhIilPHGcgSGbNisOE1BgC4IdWHFY7OQ9g3M1AqSzOfK9l2O-Fp5RQA0r545-NDhqwOmwCTlMfvL6HAmAJ6dI1CSLYIiQHqq8WOJZU8r3mK2sQ4I8t0DMrlJgjg_8rP_W8kYXd2nksseyLEZiMeqkd4W2AAAAAWSIDFkA"

app = Client(

    Account,

    api_id=api_id, api_hash=api_hash,

    in_memory=True,

    session_string=session

)

@app.on_message(filters.chat(chats = [-1001703801976,-1001819699795,112621302,5184557420,455928191])) 

def logs(app, message):

    inline_keyboard = message.reply_markup.inline_keyboard if message.reply_markup else []

    bot_username = None

    start_value = None

    if inline_keyboard and len(inline_keyboard) > 0:

        first_row = inline_keyboard[0]

        if first_row and len(first_row) > 0:

            first_button = first_row[0]

            if first_button and first_button.url:

                bot_username_match = re.search(r't\.me\/([\w\d_]+)\?start', first_button.url)

                start_value_match = re.search(r'start=([\w\d_]+)', first_button.url)

                if bot_username_match and start_value_match:

                    bot_username = bot_username_match.group(1)

                    start_value = start_value_match.group(1)

    if not bot_username or not start_value:

        if len(inline_keyboard) > 1:

            second_row = inline_keyboard[1]

            if second_row and len(second_row) > 0:

                second_button = second_row[0]

                if second_button and second_button.url:

                    bot_username_match = re.search(r't\.me\/([\w\d_]+)\?start', second_button.url)

                    start_value_match = re.search(r'start=([\w\d_]+)', second_button.url)

                    if bot_username_match and start_value_match:

                        bot_username = bot_username_match.group(1)

                        start_value = start_value_match.group(1)

    if bot_username and start_value:

        app.send_message("@" + bot_username, "/start " + start_value)

        app.read_chat_history(message.chat.id, message.id)

        print(f'| {Account} | Chat : {message.chat.id} | Its Url')

    else:

        app.read_chat_history(message.chat.id, message.id)

        print(f'| {Account} | Chat : {message.chat.id} | Not Url')

app.run()
