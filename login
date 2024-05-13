
m_login = {
    101: {'password':'101m', 'name': 'Jose'},
    102: {'password':'102m', 'name': 'Danny'},
    103: {'password':'103m', 'name': 'Rosa'},
}
c_login = {
    111: {'password':'102c', 'name':'Alex'},
    112: {'password':'103c', 'name': 'Maria'},
    113: {'password':'101c', 'name': 'Ben'},
}

def screen_two():
    pass

def reset():
    m_login.clear()
    c_login.clear()

def show_products():
    print('products')

def submit_order():
    pass

def display_orders():
    pass

def manager_display_products():
    pass

def edit_prices():
    pass

def reorder_stock():
    pass

def manager_display_products():
    pass

def logout():
    pass


is_customer = True

def login():
    global is_customer
    is_customer = int(input('Welcome to the login page! For a manager, enter 0, for customer, enter 1 >'))

    if is_customer:
        customer_portal_id = int(input('C Enter id >'))
        customer_portal_password = input('C Enter password >')
        if customer_portal_id in c_login and customer_portal_password == c_login[customer_portal_id]['password']:
            print(f'Welcome: {c_login[customer_portal_id]["name"]}')
            return True
        else:
            print('Wrong credentials. Try again')
            return False
    else:
        manager_portal_id = int(input('M Enter id >'))
        manager_portal_password = input('M Enter password >')
        if manager_portal_id in m_login and manager_portal_password == m_login[manager_portal_id]['password']:
            print(f'Welcome: {m_login[manager_portal_id]["name"]}')
            return True
        else:
            print('Wrong credentials. Try again')
            return False

def main_menu():
    while True:
        print(f'1.Login 2.Quit')
        choice = int(input('Enter 1 or 2 >'))
        if choice == 1:
            if login():
                break
        elif choice == 2:
            print('Goodbye!')
            return False
        else:
            print('Invalid choice. Please enter 1 or 2.')

    return True 

# Main program
quit_program = False

while not quit_program:
    if not main_menu():
        break
            
    if is_customer:
        while True:      
            print('1.Submit Order 2.Display order 3.Logout 4.Exit')
            choice = int(input('Enter 1, 2, 3 or 4> '))
            if choice == 1:
                submit_order()
            elif choice == 2:
                display_orders()
            elif choice == 3:
                print('Logging out...')
                break
            elif choice == 4:
                print('Exiting...')
                quit_program = True
                break
            else:
                print('Invalid choice')          
    else:
        while True:
            print('1.Display order 2.Edit prices 3.Reorder Stock 4.Logout 5.Exit')
            choice = int(input('Enter 1, 2, 3, 4 or 5> '))
            if choice == 1:
                display_orders()
            elif choice == 2:
                edit_prices()
            elif choice == 3:
                reorder_stock()
            elif choice == 4:
                print('Logging out...')
                break
            elif choice == 5:
                print('Exiting...')
                quit_program = True
                break
            else: 
                print('Invalid choice')
     
    print('Goodbye!')


 

