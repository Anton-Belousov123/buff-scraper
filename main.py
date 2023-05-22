import scraper
import sht
import tg

compare_data = []


def comparator(d):
    global compare_data
    if d not in compare_data:
        compare_data.append(d)
        return True
    return False


def main():
    while True:
        links = sht.read_links()
        for link in links:
            try:
                data = scraper.execute_link(link)
            except Exception as e:
                print('Data error')
                data = []
            for d in data:
                try:
                    is_new = comparator(d)
                    if is_new:
                        prepared_message, keyboard = tg.prepare_message_text(d)
                        tg.send_message(prepared_message, keyboard)
                except Exception as e:
                    print("Send tg error and comparation!")


if __name__ == '__main__':
    main()
