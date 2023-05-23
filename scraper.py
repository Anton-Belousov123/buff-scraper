import requests


def execute_link(link):
    responses = []
    good_id = link.split('goods/')[1].split('?')[0]
    headers = {'Cookie': 'Locale-Supported=en;'}
    url = f'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id={good_id}&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1'
    resp = requests.get(url,  headers=headers).json()
    good_info = resp['data']['goods_infos'][good_id]
    steam_price = good_info['steam_price_cny']
    name = good_info['market_hash_name']
    def_price = resp['data']['items'][0]['price']
    items = resp['data']['items']
    app_id = good_info['appid']
    for item in items:
        pattern = item['asset_info']['info']['paintseed']
        float_info = item['asset_info']['paintwear']
        buy_price = item['price']
        if len(item['asset_info']['info']['stickers']) > 0:
            class_id = item['asset_info']['classid']
            instance_id = item['asset_info']['instanceid']
            asset_id = item['asset_info']['assetid']
            url = f'https://buff.163.com/api/market/item_desc_detail?appid={app_id}&classid={class_id}&' \
                  f'instanceid={instance_id}&origin=selling-list&assetid={asset_id}&contextid=2'
            ddd = requests.get(url, headers=headers).json()
            url_to_user = ddd['data']['qr_code_url']
            stickers = ddd['data']['stickers']
            stickers_arr = []
            stickers_price = 0
            for sticker in stickers:
                sticker_price = sticker['sell_reference_price']
                sticker_name = sticker['sticker_name']
                sticker_wear = sticker['wear']
                stickers_arr.append({'name': sticker_name, 'wear': sticker_wear, 'price': sticker_price})
                if sticker_wear != 0:
                    stickers_price += float(sticker_price) * 0.03
                else:
                    stickers_price += float(sticker_price) * 0.07
            profit = (float(stickers_price) + float(buy_price)) * 0.95 - float(buy_price)
            profit_percent = (float(stickers_price) + float(buy_price)) * 0.95 / float(buy_price)
            print(profit_percent)
            if profit_percent > 0:
                responses.append({
                    'name': name,
                    'pattern': pattern,
                    'float': float_info,
                    'steam_price': steam_price,
                    'def_price': def_price,
                    'buy_price': buy_price,
                    'stickers_price': stickers_price,
                    'profit': profit,
                    'stickers': stickers_arr,
                    'url': f'https://buff.163.com/market/m/item_detail?сlassid={class_id}&'
                           f'contextid=2&goods_id={good_id}&instanceid={instance_id}&assetid={asset_id}&'
                           f'game=csgo',
                    'profit_percent': profit_percent
                })
    return responses


print(execute_link('https://buff.163.com/goods/45259?from=market#tab=selling'))