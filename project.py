""" Project Assignment.

Input: product and quantity
Output: order details
"""

import datetime
import random

#global
order_ID = 1000
products = {
    101: {'name':'headphones', 'price': 15.0},
    102: {'name':'laptop', 'price': 10.0},
    103: {'name':'pen', 'price': 3.0},
}


#functions

def compute_price(name, count):
    for pid, details in products.items():
        if details['name'] == name:
            tot_price = products[pid]['price'] * count 
        return tot_price, pid
    
def get_date():
    start = 0
    end = 365 * 4 + 1
    numbers = []
    x = start
    while x <= end:
        numbers.append(x)
        x = x + 1

    days = random.choice(numbers)

    start_date = datetime.date(2020,1,1)
    order_d = start_date + datetime.timedelta(days)

    return order_d

def submit():
    global order_ID
    #inputs
    product = input('Enter the name of product headphone, laptop or pen >')
    x = [sku['name'] for sku in products.values()]
    count = 0

    if product in x:
        count = int(input('Enter the quantity of the product >'))
        order_price = compute_price(product, count)
        date = get_date()
        order_ID += 1
        order_date_string = date.strftime("%d-%m-%y")
    else: 
        print ('Invalid. Try again.')
        submit()

    print(f'''
        product: {product} 
        count: {count} 
        total price: {order_price[0]}
        product_id: {order_price[1]}
        order_date: {order_date}
        order id: {order_ID}
            ''')

def reset():
    global order_ID
    order_ID = 10000 
    
#main
quit = False
while not quit:
    print('1.Submit 2.Reset 3.Exit')
    choice = int(input('Enter 1, or 2> '))
    if choice == 1:
        submit()
    elif choice == 2:
        reset()
    elif choice == 3:
        quit = True
    else:
        print('Invalid choice!')

print('Goodbye!')
