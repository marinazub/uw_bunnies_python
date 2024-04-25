""" Project Assignment.

Input: product and quantity
Output: order details
"""
import datetime
import random

#global
num_input = 1000

def submit():
    global num_input
    #inputs
    product = input('Enter the name of product book, notepad or pen >')
    if product == 'book' or product == 'notepad' or  product == 'pen':
        count = int(input('Enter the quantity of the product >'))
    else:
        print('Invalid choice. Enter again: book, notepad or pen>')
        count = 0
        print('1.Submit 2.Exit')
        choice = int(input('Enter 1, or 2> '))
        if choice == 1:
            submit()
        elif choice == 2:
            exit()
        else:
            print('Invalid choice!')
    #functions
    def compute_price(prodt,num):
        book_price = 15.0
        notepad_price = 8.0
        pen_price = 3.0
        if prodt == 'book':
            tot_price = book_price * num
            prod_id = 101
        elif prodt == 'notepad':
            tot_price = notepad_price * num
            prod_id = 102
        elif prodt == 'pen':
            tot_price = pen_price * num
            prod_id = 103
        else:
            tot_price = None
        
        return tot_price, prod_id
    
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
    
    #computations
    order_date = get_date()
    product_price_total = compute_price(product, count)
    #update totals
    num_input += 1

    #main
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