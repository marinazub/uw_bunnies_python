""" Project Assignment.

Input: product and quantity
Output: order details
"""

import datetime
import random

#global
order_ID = 10000

# unit dictionary
#products = {
#    101: {'name':'headphones', 'price': 15.0},
#    102: {'name':'laptop', 'price': 10.0},
#    103: {'name':'pen', 'price': 3.0},
#}

products = {
    1: {'name': 'Laptop', 'id': 101, 'price': 1000.0},
    2: {'name': 'Headphones', 'id': 102, 'price': 300.0},
    3: {'name': 'Pen', 'id': 103, 'price': 45.0}
}


#functions

#def compute_price(name, count):
#    for pid in products:
#        tot_price = products[pid]['price'] * count 
        
#    return tot_price, pid

def compute_price(prd, count):
    price = products[prd]['price']

    cost = price * count

    return cost
#end compute_cost function
    
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


def show_products():
    global products

    print('-' * 37)
    print(f'|{"Product #":^11s}|{"Name":^12s}|{"Price":^10s}|')
    print('-' * 37)
    for prd in products:
        #print(f'{prd} - {products[prd]["name"]} - ${products[prd]["price"]}')
        print(f'|{prd:^11d}|{products[prd]["name"]:>12s}|{products[prd]["price"]:>10.2f}|')
        print('-' * 37)


#end show_products function

def validate_prd(prd):
    validation_prd = False

    if prd in products.keys():
        validation_prd = True
    else:
        print('No such product in list, check below')
        show_products()

    return validation_prd

#end validate_inputs function


def validate_count( count):
    if count <= 0:
        print('Quantity must be more than 0')
        validation_count = False
    else:
        validation_count = True

    return validation_count

#end validate_inputs function

def submit():
    global order_ID, products
    #inputs
    product_validated = False
    while product_validated is False:
        try:
            product = int(input('Type 1 for laptop, 2 for earphones, 3 for charger > '))
            product_validated = validate_prd(product)
        except ValueError:
            print('Type number, please > ')


    count_validated = False
    while count_validated is False:
        try:
            count = int(input('Type amount of selected product you want to buy > '))
            count_validated = validate_count(count)
        except ValueError:
            print('Type number, please > ')      

    #product = input('Enter the name of product headphone, laptop or pen >')
    #x = [sku['name'] for sku in products.values()]
    #count = 0

    #if product in x:
    #    count = int(input('Enter the quantity of the product >'))
    #else: 
    #    print ('Invalid. Try again.')
    #    return
    #    #submit()

    order_price = compute_price(product, count)
    date = get_date()
    order_ID += 1
    order_date_string = date.strftime("%d-%m-%y")

    print(f'''
        product: {products[product]['name']} 
        count: {count} 
        total price: {order_price: .2f}
        product_id: {products[product]['id']}
        order_date: {order_date_string}
        order id: {order_ID}
            ''')

def reset():
    global order_ID
    order_ID = 10000 
    
#main
quit = False
while not quit:
    print('1.Submit 2.Reset 3.Show products 4.Exit')
    try:
        choice = int(input('Enter 1, 2, 3 or 4 > '))
        if choice == 1:
            submit()
        elif choice == 2:
            reset()
        elif choice == 3:
            show_products()
        elif choice == 4:
            quit = True
        else:
            print('Invalid choice!')
    except ValueError:
        print('Type number, please > ')

print('Goodbye!')
