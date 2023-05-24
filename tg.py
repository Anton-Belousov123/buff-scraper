import requests


def prepare_message_text(d):
    m = f"🔸{d['name']} 🔸\n➖ ➖ ➖        *INFO*        ➖ ➖ ➖\n" \
        f"Pattern: *{d['pattern']}*\nFloat: *{round(float(d['float']), 8)}*\n\nSteam price: *￥ {d['steam_price']}*\n" \
           f"Def price: *￥ {d['def_price']}*\nBuy price: *￥ {d['buy_price']}*\n\nStickers price: *￥ {round(float(d['stickers_price']), 2)}*\n" \
           f"Profit: *￥ {round(d['profit'], 2)} | {round(d['profit_percent'], 2)}%*\n\n➖ ➖ ➖    *STICKERS*    ➖ ➖ ➖"
    print(m)
    for s in d['stickers']:
        m += f'\n{s["name"]} | *￥ {s["price"]}* | *{100 - int(s["wear"])}%*'

    button_markup = {
        'inline_keyboard': [
            [{'text': "Buff 163", 'url': d['url']}],
        ]
    }
    print(button_markup)
    return m, button_markup

def send_message(message_text, button_markup):
    bot_token = '6108176723:AAH5l3ZvOnsYXRL-slGaFoAbu1fYsP6fi70'
    chat_id = '-1001837783795'
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {'chat_id': chat_id, 'text': message_text, 'parse_mode': 'Markdown',
              'reply_markup': button_markup}
    resp = requests.post(api_url, json=params)
    print(resp.text)