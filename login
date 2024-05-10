
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


def login():
    customer_login = int(input('Welcome to login portal! For manager, enter 0, for customer, enter 1 >'))

    if customer_login:
        customer_portal_id = int(input('C Enter id >'))
        customer_portal_password = input('C Enter password >')
        if customer_portal_id in c_login and customer_portal_password == c_login[customer_portal_id]['password']:
            print(f'Welcome: {c_login[customer_portal_id]["name"]}')
        else:
            print('No data. Try again')
    else:
        manager_portal_id = int(input('M Enter id >'))
        manager_portal_password = input('M Enter password >')
        if manager_portal_id in m_login and manager_portal_password == m_login[manager_portal_id]['password']:
            print(f'Welcome: {m_login[manager_portal_id]["name"]}')
        else:
            print('No data. Try again')

def reset():
    m_login.clear()
    c_login.clear()

def show_products():
    print('products')

def submit():
    pass

#main
quit = False
while not quit:
    print('0.Login 1.Show products 2.Proceed with order 3.Reset 4.Exit')
    choice = int(input('Enter 1, 2, 3 or 4> '))
    if choice == 0:
        login()
    if choice == 1:
        show_products()
    elif choice == 2:
        submit()
    elif choice == 3:
        reset()
    elif choice == 4:
        quit = True
    else:
        print('Invalid choice!')

print('Goodbye!')
