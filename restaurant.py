# Tasty Bites - Restaurant Ordering System

# ============================================================
# CLASS: MENU ITEM
# ============================================================

class MenuItem:

    def __init__(self, item_id, name, category, price):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price

    def display_item(self):
        print(
            f"{self.item_id}. "
            f"{self.name:<25} "
            f"₹{self.price}"
        )


# ============================================================
# CREATING MENU ITEMS
# ============================================================

# Starters

item1 = MenuItem(101, "French Fries", "Starter", 100)
item2 = MenuItem(102, "Chicken Nuggets", "Starter", 140)
item3 = MenuItem(103, "Garlic Bread", "Starter", 120)
item4 = MenuItem(104, "Chicken Wings", "Starter", 180)

# Main Course

item5 = MenuItem(105, "Margherita Pizza", "Main Course", 180)
item6 = MenuItem(106, "Chicken Burger", "Main Course", 150)
item7 = MenuItem(107, "Chicken Fried Rice", "Main Course", 170)
item8 = MenuItem(108, "Veg Noodles", "Main Course", 140)
item9 = MenuItem(109, "Chicken Biryani", "Main Course", 220)

# Beverages

item10 = MenuItem(110, "Fresh Lime Juice", "Beverage", 70)
item11 = MenuItem(111, "Cold Coffee", "Beverage", 110)
item12 = MenuItem(112, "Mango Shake", "Beverage", 120)
item13 = MenuItem(113, "Soft Drink", "Beverage", 60)

# Desserts

item14 = MenuItem(114, "Chocolate Cake", "Dessert", 130)
item15 = MenuItem(115, "Ice Cream", "Dessert", 90)
item16 = MenuItem(116, "Brownie", "Dessert", 120)


# ============================================================
# DATA STRUCTURES
# ============================================================

# List to store all menu items

menu_items = [
    item1, item2, item3, item4,
    item5, item6, item7, item8, item9,
    item10, item11, item12, item13,
    item14, item15, item16
]


# Dictionary for quick menu lookup

menu_dict = {}

for item in menu_items:
    menu_dict[item.item_id] = item


# List to store cart items

cart = []


# Tuple containing restaurant information

restaurant_info = (
    "Tasty Bites Restaurant",
    "Main Road, Kerala",
    "9876543210",
    "10:00 AM - 10:00 PM"
)


# Tuple containing order types

order_types = (
    "Dine-In",
    "Takeaway"
)


# Set containing payment methods

payment_methods = {
    "Cash",
    "UPI",
    "Card"
}


# Set containing special offer days

offer_days = {
    "Saturday",
    "Sunday"
}


# ============================================================
# CUSTOMER DETAILS
# ============================================================

customer_name = ""
customer_phone = ""
order_type = ""
payment_method = ""


# Starting order number

order_number = 1000


# ============================================================
# RESTAURANT INFORMATION
# ============================================================

def restaurant_information():

    print("\n")
    print("=" * 60)
    print("          🏪 RESTAURANT INFORMATION")
    print("=" * 60)

    print(f"🏪 Restaurant : {restaurant_info[0]}")
    print(f"📍 Location   : {restaurant_info[1]}")
    print(f"📞 Phone      : {restaurant_info[2]}")
    print(f"🕙 Opening    : {restaurant_info[3]}")

    print("-" * 60)

    print("🍽️ Order Types:")

    for order in order_types:
        print(f"- {order}")

    print("-" * 60)

    print("💳 Payment Methods:")

    for method in payment_methods:
        print(f"- {method}")

    print("-" * 60)

    print("🎁 Special Offer Days:")

    for day in offer_days:
        print(f"- {day}")

    print("=" * 60)


# ============================================================
# DISPLAY SPECIAL OFFERS
# ============================================================

def display_offers():

    print("\n")
    print("=" * 60)
    print("              🎁 SPECIAL OFFERS")
    print("=" * 60)

    print("💰 5% discount on orders above ₹500")
    print("💰 10% discount on orders above ₹1000")
    print("🎉 Weekend special offers available")
    print("🍰 Special dessert offers for selected orders")

    print("=" * 60)


# ============================================================
# DISPLAY MENU
# ============================================================

def display_menu():

    print("\n")
    print("🍔 TASTY BITES RESTAURANT")
    print("=" * 55)

    print("\n🍟 STARTERS")
    print("-" * 55)

    for item in menu_items:

        if item.category == "Starter":
            item.display_item()

    print("\n🍕 MAIN COURSE")
    print("-" * 55)

    for item in menu_items:

        if item.category == "Main Course":
            item.display_item()

    print("\n🥤 BEVERAGES")
    print("-" * 55)

    for item in menu_items:

        if item.category == "Beverage":
            item.display_item()

    print("\n🍰 DESSERTS")
    print("-" * 55)

    for item in menu_items:

        if item.category == "Dessert":
            item.display_item()

    print("=" * 55)


# ============================================================
# ADD ITEMS TO CART
# ============================================================

def add_to_cart():

    display_menu()

    while True:

        try:

            item_id = int(
                input(
                    "\n🛒 Enter Item ID to add "
                    "to cart (0 to finish): "
                )
            )

            if item_id == 0:
                break

            if item_id not in menu_dict:

                print(
                    "❌ Invalid Item ID. "
                    "Please try again."
                )

                continue

            quantity = int(
                input("🔢 Enter quantity: ")
            )

            if quantity <= 0:

                print(
                    "❌ Quantity must be "
                    "greater than 0."
                )

                continue

            selected_item = menu_dict[item_id]

            cart.append(
                {
                    "item": selected_item,
                    "quantity": quantity
                }
            )

            print(
                f"✅ {quantity} x "
                f"{selected_item.name} "
                f"added to cart."
            )

        except ValueError:

            print(
                "❌ Please enter numbers only."
            )


# ============================================================
# VIEW CART
# ============================================================

def view_cart():

    if not cart:

        print(
            "\n🛒 Your cart is empty."
        )

        return

    print("\n🛒 YOUR CART")
    print("=" * 70)

    print(
        f"{'Item':<25}"
        f"{'Qty':<8}"
        f"{'Price':<12}"
        f"{'Total':<12}"
    )

    print("-" * 70)

    grand_total = 0

    for cart_item in cart:

        item = cart_item["item"]
        quantity = cart_item["quantity"]

        item_total = (
            item.price * quantity
        )

        grand_total += item_total

        print(
            f"{item.name:<25}"
            f"{quantity:<8}"
            f"₹{item.price:<11}"
            f"₹{item_total:<11}"
        )

    print("-" * 70)

    print(
        f"{'💰 Grand Total':<50}"
        f" ₹{grand_total}"
    )

    print("=" * 70)


# ============================================================
# UPDATE CART
# ============================================================

def update_cart():

    if not cart:

        print(
            "\n🛒 Your cart is empty."
        )

        return

    view_cart()

    try:

        item_id = int(
            input(
                "\n✏️ Enter Item ID to update: "
            )
        )

        for cart_item in cart:

            if cart_item["item"].item_id == item_id:

                new_quantity = int(
                    input(
                        "🔢 Enter new quantity: "
                    )
                )

                if new_quantity <= 0:

                    print(
                        "❌ Quantity must be "
                        "greater than 0."
                    )

                    return

                cart_item["quantity"] = (
                    new_quantity
                )

                print(
                    "✅ Cart updated "
                    "successfully."
                )

                return

        print(
            "❌ Item not found in your cart."
        )

    except ValueError:

        print(
            "❌ Please enter a valid number."
        )


# ============================================================
# REMOVE ITEM FROM CART
# ============================================================

def remove_from_cart():

    if not cart:

        print(
            "\n🛒 Your cart is empty."
        )

        return

    view_cart()

    try:

        item_id = int(
            input(
                "\n🗑️ Enter Item ID to remove: "
            )
        )

        for cart_item in cart:

            if cart_item["item"].item_id == item_id:

                item_name = (
                    cart_item["item"].name
                )

                print(
                    f"\n⚠️ Are you sure you "
                    f"want to remove "
                    f"{item_name}?"
                )

                print("1. ✅ Yes")
                print("2. ❌ No")

                confirmation = input(
                    "Enter your choice: "
                ).strip()

                if confirmation == "1":

                    cart.remove(cart_item)

                    print(
                        f"🗑️ {item_name} "
                        f"removed from cart."
                    )

                elif confirmation == "2":

                    print(
                        "↩️ Item was not removed."
                    )

                else:

                    print(
                        "❌ Invalid choice. "
                        "Item was not removed."
                    )

                return

        print(
            "❌ Item not found in your cart."
        )

    except ValueError:

        print(
            "❌ Please enter a valid number."
        )


# ============================================================
# CLEAR CART
# ============================================================

def clear_cart():

    if not cart:

        print(
            "\n🛒 Your cart is already empty."
        )

        return

    view_cart()

    print(
        "\n⚠️ Are you sure you want "
        "to clear the cart?"
    )

    print("1. ✅ Yes")
    print("2. ❌ No")

    choice = input(
        "Enter your choice: "
    ).strip()

    if choice == "1":

        cart.clear()

        print(
            "🧹 All items have been "
            "removed from the cart."
        )

    elif choice == "2":

        print(
            "↩️ Cart was not cleared."
        )

    else:

        print(
            "❌ Invalid choice. "
            "Cart was not cleared."
        )


# ============================================================
# GET CUSTOMER DETAILS
# ============================================================

def get_customer_details():

    global customer_name
    global customer_phone
    global order_type
    global payment_method

    print("\n👤 CUSTOMER DETAILS")
    print("=" * 45)

    # Customer name

    while True:

        customer_name = input(
            "👤 Enter your name: "
        ).strip()

        if customer_name:

            break

        print(
            "❌ Name cannot be empty."
        )

    # Phone number

    while True:

        customer_phone = input(
            "📞 Enter your phone number: "
        ).strip()

        if (
            customer_phone.isdigit()
            and len(customer_phone) == 10
        ):

            break

        print(
            "❌ Please enter a valid "
            "10-digit phone number."
        )

    # Order type

    print("\n🍽️ ORDER TYPE")

    for index, order in enumerate(
        order_types,
        start=1
    ):

        print(
            f"{index}. {order}"
        )

    while True:

        try:

            choice = int(
                input(
                    "👉 Enter your choice: "
                )
            )

            if choice == 1:

                order_type = order_types[0]

                break

            elif choice == 2:

                order_type = order_types[1]

                break

            else:

                print(
                    "❌ Please select "
                    "1 or 2."
                )

        except ValueError:

            print(
                "❌ Please enter a number."
            )

    # Payment method

    print("\n💳 PAYMENT METHOD")

    print("1. 💵 Cash")
    print("2. 📱 UPI")
    print("3. 💳 Card")

    while True:

        try:

            payment_choice = int(
                input(
                    "👉 Enter payment method: "
                )
            )

            if payment_choice == 1:

                payment_method = "Cash"

                break

            elif payment_choice == 2:

                payment_method = "UPI"

                break

            elif payment_choice == 3:

                payment_method = "Card"

                break

            else:

                print(
                    "❌ Please select "
                    "1, 2, or 3."
                )

        except ValueError:

            print(
                "❌ Please enter "
                "a valid number."
            )


# ============================================================
# SAVE ORDER TO TEXT FILE
# ============================================================

def save_order_to_file(
    order_id,
    subtotal,
    discount,
    gst,
    final_amount
):

    try:

        with open(
            "order_history.txt",
            "a",
            encoding="utf-8"
        ) as file:

            file.write("\n")

            file.write(
                "=" * 55 + "\n"
            )

            file.write(
                "              🍔 TASTY BITES\n"
            )

            file.write(
                "              🧾 ORDER BILL\n"
            )

            file.write(
                "=" * 55 + "\n"
            )

            file.write(
                f"🆔 Order ID: {order_id}\n"
            )

            file.write(
                f"👤 Customer Name: "
                f"{customer_name}\n"
            )

            file.write(
                f"📞 Phone Number: "
                f"{customer_phone}\n"
            )

            file.write(
                f"🍽️ Order Type: "
                f"{order_type}\n"
            )

            file.write(
                f"💳 Payment Method: "
                f"{payment_method}\n"
            )

            file.write(
                "-" * 55 + "\n"
            )

            for cart_item in cart:

                item = cart_item["item"]
                quantity = cart_item["quantity"]

                item_total = (
                    item.price * quantity
                )

                file.write(
                    f"{item.name} | "
                    f"Quantity: {quantity} | "
                    f"Price: ₹{item.price} | "
                    f"Total: "
                    f"₹{item_total:.2f}\n"
                )

            file.write(
                "-" * 55 + "\n"
            )

            file.write(
                f"Subtotal: "
                f"₹{subtotal:.2f}\n"
            )

            file.write(
                f"Discount: "
                f"₹{discount:.2f}\n"
            )

            file.write(
                f"GST (5%): "
                f"₹{gst:.2f}\n"
            )

            file.write(
                f"Final Amount: "
                f"₹{final_amount:.2f}\n"
            )

            file.write(
                "=" * 55 + "\n"
            )

        print(
            "💾 Complete order saved "
            "to order_history.txt"
        )

    except OSError:

        print(
            "❌ Unable to save order "
            "to file."
        )


# ============================================================
# GENERATE BILL
# ============================================================

def generate_bill():

    global order_number

    if not cart:

        print(
            "\n🛒 Your cart is empty."
        )

        print(
            "⚠️ Please add items before "
            "placing an order."
        )

        return

    # Generate order ID

    order_number += 1

    current_order_id = (
        f"TB{order_number}"
    )

    # Get customer details

    get_customer_details()

    subtotal = 0

    print("\n")

    print("=" * 70)

    print(
        "                 🧾 FINAL BILL"
    )

    print(
        "                 🍔 TASTY BITES"
    )

    print("=" * 70)

    print(
        f"🆔 Order ID       : "
        f"{current_order_id}"
    )

    print(
        f"👤 Customer Name  : "
        f"{customer_name}"
    )

    print(
        f"📞 Phone Number   : "
        f"{customer_phone}"
    )

    print(
        f"🍽️ Order Type     : "
        f"{order_type}"
    )

    print(
        f"💳 Payment Method : "
        f"{payment_method}"
    )

    print("-" * 70)

    print(
        f"{'Item':<25}"
        f"{'Qty':<8}"
        f"{'Price':<12}"
        f"{'Total':<12}"
    )

    print("-" * 70)

    # Calculate subtotal

    for cart_item in cart:

        item = cart_item["item"]
        quantity = cart_item["quantity"]

        item_total = (
            item.price * quantity
        )

        subtotal += item_total

        print(
            f"{item.name:<25}"
            f"{quantity:<8}"
            f"₹{item.price:<11}"
            f"₹{item_total:<11}"
        )

    # Calculate discount

    if subtotal >= 1000:

        discount = subtotal * 0.10

    elif subtotal >= 500:

        discount = subtotal * 0.05

    else:

        discount = 0

    discounted_amount = (
        subtotal - discount
    )

    # Calculate GST

    gst = discounted_amount * 0.05

    # Calculate final amount

    final_amount = (
        discounted_amount + gst
    )

    print("-" * 70)

    print(
        f"{'💰 Subtotal':<52}"
        f" ₹{subtotal:.2f}"
    )

    print(
        f"{'🎁 Discount':<52}"
        f" ₹{discount:.2f}"
    )

    print(
        f"{'🧾 GST (5%)':<52}"
        f" ₹{gst:.2f}"
    )

    print("-" * 70)

    print(
        f"{'💵 FINAL AMOUNT':<52}"
        f" ₹{final_amount:.2f}"
    )

    print("=" * 70)

    # Save order

    save_order_to_file(
        current_order_id,
        subtotal,
        discount,
        gst,
        final_amount
    )

    print("\n🎉 ORDER CONFIRMED!")

    print(
        f"🆔 Your Order ID: "
        f"{current_order_id}"
    )

    print(
        f"💳 Payment Method: "
        f"{payment_method}"
    )

    print(
        "💾 Order saved successfully."
    )

    print(
        "🙏 Thank you for ordering "
        "from Tasty Bites!"
    )

    # Clear cart after successful order

    cart.clear()


# ============================================================
# VIEW ORDER HISTORY
# ============================================================

def view_order_history():

    try:

        with open(
            "order_history.txt",
            "r",
            encoding="utf-8"
        ) as file:

            history = file.read()

        if history.strip():

            print("\n")

            print("=" * 60)

            print(
                "               📋 ORDER HISTORY"
            )

            print("=" * 60)

            print(history)

            print("=" * 60)

        else:

            print(
                "\n📋 No order history found."
            )

    except FileNotFoundError:

        print(
            "\n📋 No orders have "
            "been placed yet."
        )

    except OSError:

        print(
            "\n❌ Unable to read "
            "order history."
        )


# ============================================================
# SEARCH ORDER
# ============================================================

def search_order():

    search_id = input(
        "\n🔍 Enter Order ID to search: "
    ).strip().upper()

    try:

        with open(
            "order_history.txt",
            "r",
            encoding="utf-8"
        ) as file:

            history = file.read()

        orders = history.split(
            "=" * 55
        )

        found = False

        for order in orders:

            if (
                f"🆔 Order ID: {search_id}"
                in order
            ):

                print("\n")

                print("=" * 60)

                print(
                    "                 🔍 ORDER FOUND"
                )

                print("=" * 60)

                print(
                    order.strip()
                )

                print("=" * 60)

                found = True

                break

        if not found:

            print(
                f"\n❌ No order found "
                f"with Order ID: "
                f"{search_id}"
            )

    except FileNotFoundError:

        print(
            "\n📋 No order history found."
        )

    except OSError:

        print(
            "\n❌ Unable to read "
            "order history."
        )


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():

    # Dictionary to display selected menu option

    choice_names = {

        1: "View Menu",
        2: "Add Items to Cart",
        3: "View Cart",
        4: "Update Cart",
        5: "Remove Item",
        6: "Clear Cart",
        7: "Place Order & Generate Bill",
        8: "View Order History",
        9: "Search Order",
        10: "Restaurant Information",
        11: "Special Offers",
        12: "Exit"
    }

    while True:

        print("\n")

        print("=" * 50)

        print(
            "             🍔 TASTY BITES 🍔"
        )

        print("=" * 50)

        print("1.  📋 View Menu")
        print("2.  🛒 Add Items to Cart")
        print("3.  👀 View Cart")
        print("4.  ✏️  Update Cart")
        print("5.  🗑️  Remove Item")
        print("6.  🧹 Clear Cart")
        print("7.  🧾 Place Order & Generate Bill")
        print("8.  📜 View Order History")
        print("9.  🔍 Search Order")
        print("10. 🏪 Restaurant Information")
        print("11. 🎁 Special Offers")
        print("12. ❌ Exit")

        print("=" * 50)

        try:

            choice = int(
                input(
                    "👉 Enter your choice: "
                )
            )

            # Display selected choice

            if choice in choice_names:

                print(
                    f"➡️ Entered Choice: "
                    f"{choice} - "
                    f"{choice_names[choice]}"
                )

            if choice == 1:

                display_menu()

            elif choice == 2:

                add_to_cart()

            elif choice == 3:

                view_cart()

            elif choice == 4:

                update_cart()

            elif choice == 5:

                remove_from_cart()

            elif choice == 6:

                clear_cart()

            elif choice == 7:

                generate_bill()

            elif choice == 8:

                view_order_history()

            elif choice == 9:

                search_order()

            elif choice == 10:

                restaurant_information()

            elif choice == 11:

                display_offers()

            elif choice == 12:

                print(
                    "\n🙏 Thank you for "
                    "visiting Tasty Bites!"
                )

                print(
                    "👋 Have a great day!"
                )

                break

            else:

                print(
                    "❌ Invalid choice. "
                    "Please select 1-12."
                )

        except ValueError:

            print(
                "❌ Please enter "
                "a valid number."
            )


# ============================================================
# START THE APPLICATION
# ============================================================

print(
    "\n" + "=" * 60
)

print(
    "          🍔 WELCOME TO TASTY BITES 🍔"
)

print(
    "          🍽️ Your Favourite Food Place!"
)

print(
    "=" * 60
)

main_menu()
