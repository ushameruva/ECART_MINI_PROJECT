def login():
    print("----------------E-CART LOGIN----------------")
    print("1. E-Cart Login (Admin)")
    print("2. User Login")
    choice = input("Select login type: ")

    if choice == '1':
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username == 'admin' and password == 'admin123':
            return 'admin'
    elif choice == '2':
        return 'user'
    return None
