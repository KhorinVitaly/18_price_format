def format_price(price):
    if not isinstance(price, (float, int, str)):
        return None

    if isinstance(price, str):
        try:
            price = float(price)
        except ValueError:
            return None

    if isinstance(price, float) and price % 1 == 0:
        price = int(price)

    return '{:,}'.format(price).replace(',', ' ')

if __name__ == '__main__':
    price = format_price(input('input price to format: '))
    if price:
        print('formatted price: ' + format_price(price))
    else:
        print('incorrect input')
