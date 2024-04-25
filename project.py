""" Project Assignment.

Input: product and quantity
Output: order details
"""
import datetime
import random

#global
num_input = 1000
products = = {
    101: {'name':'book', 'price': 15.0},
    102: {'name':'notepad', 'price': 10.0},
    103: {'name':'pen', 'price': 3.0},
}


#functions

def compute_price(name, count):
    for pid, details in products.items():
        if details['name'] == name:
            tot_price = products[pid]['price'] * count 
        return tot_price, pid
    
def get_date():
    start = 2020
    end = 2023
    numbers = []
    x = start
    while x <= end:
        numbers.append(x)
        x = x + 1

    choice = random.choice(numbers)
    return choice

def submit():
    global num_input
    #inputs
    product = input('Enter the name of product book, notepad or pen >')
    for pid, details in products.items():
        if details['name'] == product:
            count = int(input('Enter the quantity of the product >'))
        #else:
           # print('Invalid choice. Enter again: book, notepad or pen>')
           # count = 0
           # print('1.Submit 2.Exit')
           # choice = int(input('Enter 1, or 2> '))
           # if choice == 1:
            #    submit()
           #elif choice == 2:
           #     exit()
           # else:
           #     print('Invalid choice!')
   
    #computations
    order_date = get_date()
    product_price_total = compute_price(product, count)
    #update totals
    num_input += 1

    print(f'''
        product: {product} 
        count: {count} 
        total price: {product_price_total[0]}
        product_id: {product_price_total[1]}
        order_date: {order_date}
        order id: {num_input}
            ''')
    
#main
quit = False
while not quit:
    print('1.Submit 2.Exit')
    choice = int(input('Enter 1, or 2> '))
    if choice == 1:
        submit()
    elif choice == 2:
        quit = True
    else:
        print('Invalid choice!')

print('Goodbye!')
