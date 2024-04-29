""" Project Assignment.

Input: product and quantity
Output: order details
"""

#global
order_ID = 1000
products = {
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
    global order_ID
    #inputs
    product = input('Enter the name of product headphone, laptop or pen >')
    x = [sku['name'] for sku in items.values()]
    count = 0

    if product in x:
        count = int(input('Enter the quantity of the product >'))
        #order_price = compute_order_price(product, count)
        #date = get_date()
        order_ID += 1
        #order_date_string = date.strftime("%d-%m-%y")
    else: 
        print ('Invalid. Try again.')
        submit()

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
