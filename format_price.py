def format_price(price):
    if not type(price) == int and not type(price) == float:
        return None
    if type(price) == float and price % 1 == 0:
        price = int(price)
    return '{:,}'.format(price).replace(',', ' ')

if __name__ == '__main__':
    try:
        price = float(input('input price to format: '))
        print('formatted price: ' + format_price(price))
    except ValueError:
        print('incorrect input')
