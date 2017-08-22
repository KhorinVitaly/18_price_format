def format_price(price):
    try:
        if price % 1 == 0:
            price = int(price)
        return '{0:,}'.format(price).replace(',', ' ')
    except TypeError:
        return None

if __name__ == '__main__':
    try:
        price = float(input('input price to format: '))
        print('formatted price: ' + format_price(price))
    except ValueError:
        print('incorrect input')