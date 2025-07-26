from database import get_connection
from login import login

def add_item():
    conn = get_connection()
    cursor = conn.cursor()
    item_id = int(input("Enter item ID: "))
    item_name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    cursor.execute("INSERT INTO items VALUES (%s, %s, %s, %s)", (item_id, item_name, price, quantity))
    conn.commit()
    print("Item added successfully.")
    conn.close()

def update_item():
    conn = get_connection()
    cursor = conn.cursor()
    item_id = int(input("Enter item ID to update: "))
    price = float(input("Enter new price: "))
    quantity = int(input("Enter new quantity: "))
    cursor.execute("UPDATE items SET price=%s, quantity=%s WHERE item_id=%s", (price, quantity, item_id))
    conn.commit()
    print("Item updated successfully.....🔄👍")
    conn.close()
def accept_order():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    if not orders:
        print("No pending orders.")
        conn.close()
        return

    print("\nPending Orders:")
    for order in orders:
        print(f"Order ID: {order[0]}, Item ID: {order[1]}, Item Name: {order[2]}, Quantity: {order[3]}")

    order_id = int(input("Enter Order ID to accept: "))

    cursor.execute("SELECT * FROM orders WHERE order_id = %s", (order_id,))
    order = cursor.fetchone()

    if order:
        cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
        conn.commit()
        print("......Order accepted and removed from pending list......")
    else:
        print("Order not found.")

    conn.close()

def remove_item():
    conn = get_connection()
    cursor = conn.cursor()
    item_id = int(input("Enter item ID to delete: "))
    cursor.execute("DELETE FROM items WHERE item_id=%s", (item_id,))
    conn.commit()
    print("Item removed successfully🚮..........")
    conn.close()

def view_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def place_order():
    conn = get_connection()
    cursor = conn.cursor()
    view_items()
    item_id = int(input("Enter item ID to order: "))
    quantity = int(input("Enter quantity to order: "))
    cursor.execute("SELECT item_name, quantity FROM items WHERE item_id=%s", (item_id,))
    result = cursor.fetchone()
    if result:
        item_name, available_qty = result
        if available_qty >= quantity:
            cursor.execute("INSERT INTO orders (item_id, item_name, quantity) VALUES (%s, %s, %s)",
                           (item_id, item_name, quantity))
            cursor.execute("UPDATE items SET quantity=quantity - %s WHERE item_id=%s", (quantity, item_id))
            conn.commit()
            print("Order placed successfully........🎉👍")
        else:
            print("Not enough quantity available.......👎😞")
    else:
        print("Item not found.❌")
    conn.close()

def remove_order():
    conn = get_connection()
    cursor = conn.cursor()
    order_id = int(input("Enter order ID to remove: "))
    cursor.execute("SELECT item_id, quantity FROM orders WHERE order_id=%s", (order_id,))
    result = cursor.fetchone()
    if result:
        item_id, quantity = result
        cursor.execute("DELETE FROM orders WHERE order_id=%s", (order_id,))
        cursor.execute("UPDATE items SET quantity=quantity + %s WHERE item_id=%s", (quantity, item_id))
        conn.commit()
        print("Order removed and stock updated......👍")
    else:
        print("Order not found.....❌")
    conn.close()
1
def view_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def main():
    user = login()
    if user == 'admin':
        while True:
            
            
            print("\n1. Add Item\n2. Update Item\n3. Remove Item\n4. View Items\n5. View Orders\n6. Accept Order\n7. Remove Order\n8. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                add_item()
            elif choice == '2':
                update_item()
            elif choice == '3':
                remove_item()
            elif choice == '4':
                view_items()
            elif choice == '5':
                view_orders()
            elif choice == '6':
                accept_order()
            elif choice == '7':
                remove_order()
            elif choice == '8':
                break

    elif user == 'user':
        while True:
            print(" --------------- 🎊 E-CART SHOPPING 🎊-------------------")
            print("\n1. View Items\n2. Place Order\n3. Remove Order\n4. My orders \n5. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                view_items()
            elif choice == '2':
                place_order()
            elif choice == '3':
                remove_order()
            elif choice == '4':
                view_orders()
            elif choice == '5':
                break
    else:
        print("Invalid login.")

if __name__ == "__main__":
    main()
