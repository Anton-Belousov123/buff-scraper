def prepare_message_text(d):
    m = f"🔸{d['name']} 🔸\n➖ ➖ ➖        *INFO*        ➖ ➖ ➖\n" \
        f"Pattern: *{d['pattern']}* ({d['idx']})\nFloat: *{round(float(d['float']), 8)}*\n\nSteam price: *￥ {d['steam_price']}*\n" \
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
    return m.encode('utf-8'), button_markup
