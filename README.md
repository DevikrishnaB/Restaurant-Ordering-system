# Restaurant-Ordering-system
# 🍔 Tasty Bites - Restaurant Ordering System

A simple **Python-based restaurant ordering system** that allows users to view the menu, add items to a cart, update or remove items, place orders, generate bills, and maintain order history.
The main objective of this project is to build a simple restaurant ordering system using Python while practicing **Object-Oriented Programming, data structures, functions, loops, conditional statements, exception handling, and file handling**.

## ✨ Features

* 📋 View restaurant menu
* 🛒 Add items to cart
* 👀 View cart
* ✏️ Update cart items
* 🗑️ Remove items from cart
* 🧹 Clear cart
* 🧾 Generate final bill
* 💰 Automatic discount calculation
* 🧮 GST calculation
* 💾 Save orders to a text file
* 📜 View order history
* 🔍 Search orders using Order ID
* 🏪 View restaurant information
* 🎁 View special offers
* 💳 Multiple payment methods
* 🍽️ Dine-In and Takeaway options

## 📂 Project Structure

```text
Tasty-Bites/
│
├── main.py
├── order_history.txt
└── README.md
```

## 🍽️ How It Works

### 1. View Menu

Users can view all available food items along with their item IDs, categories, and prices.

### 2. Add Items to Cart

Enter the item ID and quantity to add food items to the cart.

### 3. Manage Cart

Users can:

* 👀 View cart
* ✏️ Update item quantity
* 🗑️ Remove an item
* 🧹 Clear the entire cart

### 4. Place Order

After selecting the required items, users can enter:

* 👤 Customer name
* 📞 Phone number
* 🍽️ Order type
* 💳 Payment method

### 5. Generate Bill

The system automatically calculates:

* 💰 Subtotal
* 🎁 Discount
* 🧾 GST
* 💵 Final amount

### 6. Order History

Every confirmed order is saved in `order_history.txt`.

Each order receives a unique Order ID such as:

```text
TB1001
TB1002
TB1003
```

Orders can also be searched using their Order ID.

## 💸 Discount Rules

| Order Amount    |    Discount |
| --------------- | ----------: |
| Below ₹500      | No Discount |
| ₹500 - ₹999     |          5% |
| ₹1000 and above |         10% |

GST of **5%** is calculated after applying the discount.

## 💳 Payment Methods

* 💵 Cash
* 📱 UPI
* 💳 Card

## 🍽️ Order Types

* 🪑 Dine-In
* 🛍️ Takeaway

## 🎁 Special Offers

* 💰 5% discount on orders above ₹500
* 💰 10% discount on orders above ₹1000
* 🎉 Weekend special offers
* 🍰 Special dessert offers

## 📄 Order History

All successfully placed orders are stored in:

```text
order_history.txt
```

The file contains customer details, ordered items, payment method, subtotal, discount, GST, and final amount.

```text
**SAMPLE OUTPUT**
```

============================================================
          🍔 WELCOME TO TASTY BITES 🍔
          🍽️ Your Favourite Food Place!
============================================================
1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 1
➡️ Entered Choice: 1 - View Menu

🍔 TASTY BITES RESTAURANT

🍟 STARTERS
-------------------------------------------------------
101. French Fries              ₹100
102. Chicken Nuggets           ₹140
103. Garlic Bread              ₹120
104. Chicken Wings             ₹180

🍕 MAIN COURSE
-------------------------------------------------------
105. Margherita Pizza          ₹180
106. Chicken Burger            ₹150
107. Chicken Fried Rice        ₹170
108. Veg Noodles               ₹140
109. Chicken Biryani           ₹220

🥤 BEVERAGES
-------------------------------------------------------
110. Fresh Lime Juice          ₹70
111. Cold Coffee               ₹110
112. Mango Shake               ₹120
113. Soft Drink                ₹60

🍰 DESSERTS
-------------------------------------------------------
114. Chocolate Cake            ₹130
115. Ice Cream                 ₹90
116. Brownie                   ₹120
=======================================================


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 2
➡️ Entered Choice: 2 - Add Items to Cart

🍔 TASTY BITES RESTAURANT

🍟 STARTERS
-------------------------------------------------------
101. French Fries              ₹100
102. Chicken Nuggets           ₹140
103. Garlic Bread              ₹120
104. Chicken Wings             ₹180

🍕 MAIN COURSE
-------------------------------------------------------
105. Margherita Pizza          ₹180
106. Chicken Burger            ₹150
107. Chicken Fried Rice        ₹170
108. Veg Noodles               ₹140
109. Chicken Biryani           ₹220

🥤 BEVERAGES
-------------------------------------------------------
110. Fresh Lime Juice          ₹70
111. Cold Coffee               ₹110
112. Mango Shake               ₹120
113. Soft Drink                ₹60

🍰 DESSERTS
-------------------------------------------------------
114. Chocolate Cake            ₹130
115. Ice Cream                 ₹90
116. Brownie                   ₹120
=======================================================

🛒 Enter Item ID to add to cart (0 to finish): 104
🔢 Enter quantity: 1
✅ 1 x Chicken Wings added to cart.

🛒 Enter Item ID to add to cart (0 to finish): 110
🔢 Enter quantity: 2
✅ 2 x Fresh Lime Juice added to cart.

🛒 Enter Item ID to add to cart (0 to finish): 114
🔢 Enter quantity: 1
✅ 1 x Chocolate Cake added to cart.

🛒 Enter Item ID to add to cart (0 to finish): 0


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 3
➡️ Entered Choice: 3 - View Cart

🛒 YOUR CART
======================================================
Item                     Qty     Price       Total
------------------------------------------------------
Chicken Wings            1       ₹180        ₹180
Fresh Lime Juice         2       ₹70         ₹140
Chocolate Cake           1       ₹130        ₹130
------------------------------------------------------
💰 Grand Total                                      ₹450
======================================================


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 4
➡️ Entered Choice: 4 - Update Cart

🛒 YOUR CART
======================================================
Item                     Qty     Price       Total
------------------------------------------------------
Chicken Wings            1       ₹180        ₹180
Fresh Lime Juice         2       ₹70         ₹140
Chocolate Cake           1       ₹130        ₹130
------------------------------------------------------
💰 Grand Total                                      ₹450
======================================================

✏️ Enter Item ID to update: 110
🔢 Enter new quantity: 1
✅ Cart updated successfully.


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 5
➡️ Entered Choice: 5 - Remove Item

🛒 YOUR CART
======================================================
Item                     Qty     Price       Total
------------------------------------------------------
Chicken Wings            1       ₹180        ₹180
Fresh Lime Juice         1       ₹70         ₹70
Chocolate Cake           1       ₹130        ₹130
------------------------------------------------------
💰 Grand Total                                      ₹380
======================================================

🗑️ Enter Item ID to remove: 114

⚠️ Are you sure you want to remove Chocolate Cake?

1. ✅ Yes
2. ❌ No
👉 Enter your choice: 1
🗑️ Chocolate Cake removed from cart.


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 7
➡️ Entered Choice: 7 - Place Order & Generate Bill

👤 CUSTOMER DETAILS
=============================================
👤 Enter your name: Devikrishna B
📞 Enter your phone number: 1122334455

🍽️ ORDER TYPE
1. Dine-In
2. Takeaway
👉 Enter your choice: 1

💳 PAYMENT METHOD
1. 💵 Cash
2. 📱 UPI
3. 💳 Card
👉 Enter payment method: 2

🧾 FINAL BILL
======================================================================
🆔 Order ID       : TB1001
👤 Customer Name  : Devikrishna B
📞 Phone Number   : 1122334455
🍽️ Order Type     : Dine-In
💳 Payment Method : UPI
----------------------------------------------------------------------
Item                     Qty     Price       Total
----------------------------------------------------------------------
Chicken Wings            1       ₹180        ₹180
Fresh Lime Juice         1       ₹70         ₹70
----------------------------------------------------------------------
💰 Subtotal                                      ₹250.00
🎁 Discount                                        ₹0.00
🧾 GST (5%)                                       ₹12.50
----------------------------------------------------------------------
💵 FINAL AMOUNT                                  ₹262.50
======================================================================

💾 Complete order saved to order_history.txt

🎉 ORDER CONFIRMED!
🆔 Your Order ID: TB1001
💳 Payment Method: UPI
💾 Order saved successfully.
🙏 Thank you for ordering from Tasty Bites!


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 2
➡️ Entered Choice: 2 - Add Items to Cart

🍔 TASTY BITES RESTAURANT

🍟 STARTERS
-------------------------------------------------------
101. French Fries              ₹100
102. Chicken Nuggets           ₹140
103. Garlic Bread              ₹120
104. Chicken Wings             ₹180

🍕 MAIN COURSE
-------------------------------------------------------
105. Margherita Pizza          ₹180
106. Chicken Burger            ₹150
107. Chicken Fried Rice        ₹170
108. Veg Noodles               ₹140
109. Chicken Biryani           ₹220

🥤 BEVERAGES
-------------------------------------------------------
110. Fresh Lime Juice          ₹70
111. Cold Coffee               ₹110
112. Mango Shake               ₹120
113. Soft Drink                ₹60

🍰 DESSERTS
-------------------------------------------------------
114. Chocolate Cake            ₹130
115. Ice Cream                 ₹90
116. Brownie                   ₹120
=======================================================

🛒 Enter Item ID to add to cart (0 to finish): 112
🔢 Enter quantity: 1
✅ 1 x Mango Shake added to cart.

🛒 Enter Item ID to add to cart (0 to finish): 116
🔢 Enter quantity: 1
✅ 1 x Brownie added to cart.

🛒 Enter Item ID to add to cart (0 to finish): 0


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 7
➡️ Entered Choice: 7 - Place Order & Generate Bill

👤 CUSTOMER DETAILS
=============================================
👤 Enter your name: Bindu
📞 Enter your phone number: 9988776655

🍽️ ORDER TYPE
1. Dine-In
2. Takeaway
👉 Enter your choice: 2

💳 PAYMENT METHOD
1. 💵 Cash
2. 📱 UPI
3. 💳 Card
👉 Enter payment method: 1

🧾 FINAL BILL
======================================================================
🆔 Order ID       : TB1002
👤 Customer Name  : Bindu
📞 Phone Number   : 9988776655
🍽️ Order Type     : Takeaway
💳 Payment Method : Cash
----------------------------------------------------------------------
Item                     Qty     Price       Total
----------------------------------------------------------------------
Mango Shake              1       ₹120        ₹120
Brownie                  1       ₹120        ₹120
----------------------------------------------------------------------
💰 Subtotal                                      ₹240.00
🎁 Discount                                        ₹0.00
🧾 GST (5%)                                       ₹12.00
----------------------------------------------------------------------
💵 FINAL AMOUNT                                  ₹252.00
======================================================================

💾 Complete order saved to order_history.txt

🎉 ORDER CONFIRMED!
🆔 Your Order ID: TB1002
💳 Payment Method: Cash
💾 Order saved successfully.
🙏 Thank you for ordering from Tasty Bites!


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 11
➡️ Entered Choice: 11 - Special Offers

🎁 SPECIAL OFFERS
============================================================
💰 5% discount on orders above ₹500
💰 10% discount on orders above ₹1000
🎉 Weekend special offers available
🍰 Special dessert offers for selected orders
============================================================


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 10
➡️ Entered Choice: 10 - Restaurant Information

🏪 RESTAURANT INFORMATION
============================================================
🏪 Restaurant : Tasty Bites Restaurant
📍 Location   : Main Road, Kerala
📞 Phone      : 9876543210
🕙 Opening    : 10:00 AM - 10:00 PM
------------------------------------------------------------
🍽️ Order Types:
- Dine-In
- Takeaway
------------------------------------------------------------
💳 Payment Methods:
- Cash
- UPI
- Card
------------------------------------------------------------
🎁 Special Offer Days:
- Saturday
- Sunday
============================================================


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 8
➡️ Entered Choice: 8 - View Order History

📋 ORDER HISTORY
============================================================
[Previous saved orders will be displayed here]
============================================================


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 2
➡️ Entered Choice: 2 - Add Items to Cart

🍔 TASTY BITES RESTAURANT

🍟 STARTERS
-------------------------------------------------------
101. French Fries              ₹100
102. Chicken Nuggets           ₹140
103. Garlic Bread              ₹120
104. Chicken Wings             ₹180

🍕 MAIN COURSE
-------------------------------------------------------
105. Margherita Pizza          ₹180
106. Chicken Burger            ₹150
107. Chicken Fried Rice        ₹170
108. Veg Noodles               ₹140
109. Chicken Biryani           ₹220

🥤 BEVERAGES
-------------------------------------------------------
110. Fresh Lime Juice          ₹70
111. Cold Coffee               ₹110
112. Mango Shake               ₹120
113. Soft Drink                ₹60

🍰 DESSERTS
-------------------------------------------------------
114. Chocolate Cake            ₹130
115. Ice Cream                 ₹90
116. Brownie                   ₹120
=======================================================

🛒 Enter Item ID to add to cart (0 to finish): 105
🔢 Enter quantity: 1
✅ 1 x Margherita Pizza added to cart.

🛒 Enter Item ID to add to cart (0 to finish): 113
🔢 Enter quantity: 1
✅ 1 x Soft Drink added to cart.

🛒 Enter Item ID to add to cart (0 to finish): 0

1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 7
➡️ Entered Choice: 7 - Place Order & Generate Bill

👤 CUSTOMER DETAILS
=============================================
👤 Enter your name: Shiva
📞 Enter your phone number: 5566774433

🍽️ ORDER TYPE
1. Dine-In
2. Takeaway
👉 Enter your choice: 2

💳 PAYMENT METHOD
1. 💵 Cash
2. 📱 UPI
3. 💳 Card
👉 Enter payment method: 1

🧾 FINAL BILL
======================================================================
🆔 Order ID       : TB1003
👤 Customer Name  : Shiva
📞 Phone Number   : 5566774433
🍽️ Order Type     : Takeaway
💳 Payment Method : Cash
----------------------------------------------------------------------
Item                     Qty     Price       Total
----------------------------------------------------------------------
Margherita Pizza         1       ₹180        ₹180
Soft Drink               1       ₹60         ₹60
----------------------------------------------------------------------
💰 Subtotal                                      ₹240.00
🎁 Discount                                        ₹0.00
🧾 GST (5%)                                       ₹12.00
----------------------------------------------------------------------
💵 FINAL AMOUNT                                  ₹252.00
======================================================================

💾 Complete order saved to order_history.txt

🎉 ORDER CONFIRMED!
🆔 Your Order ID: TB1003
💳 Payment Method: Cash
💾 Order saved successfully.
🙏 Thank you for ordering from Tasty Bites!


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 9
➡️ Entered Choice: 9 - Search Order

🔍 Enter Order ID to search: TB1001

🔎 ORDER FOUND
============================================================
[Order details for TB1001 will be displayed here]
============================================================


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 2
➡️ Entered Choice: 2 - Add Items to Cart

🍔 TASTY BITES RESTAURANT

🍟 STARTERS
-------------------------------------------------------
101. French Fries              ₹100
102. Chicken Nuggets           ₹140
103. Garlic Bread              ₹120
104. Chicken Wings             ₹180

🍕 MAIN COURSE
-------------------------------------------------------
105. Margherita Pizza          ₹180
106. Chicken Burger            ₹150
107. Chicken Fried Rice        ₹170
108. Veg Noodles               ₹140
109. Chicken Biryani           ₹220

🥤 BEVERAGES
-------------------------------------------------------
110. Fresh Lime Juice          ₹70
111. Cold Coffee               ₹110
112. Mango Shake               ₹120
113. Soft Drink                ₹60

🍰 DESSERTS
-------------------------------------------------------
114. Chocolate Cake            ₹130
115. Ice Cream                 ₹90
116. Brownie                   ₹120
=======================================================

🛒 Enter Item ID to add to cart (0 to finish): 115
🔢 Enter quantity: 1
✅ 1 x Ice Cream added to cart.

🛒 Enter Item ID to add to cart (0 to finish): 0


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 7
➡️ Entered Choice: 7 - Place Order & Generate Bill

👤 CUSTOMER DETAILS
=============================================
👤 Enter your name: Adithyan
📞 Enter your phone number: 2299001122

🍽️ ORDER TYPE
1. Dine-In
2. Takeaway
👉 Enter your choice: 2

💳 PAYMENT METHOD
1. 💵 Cash
2. 📱 UPI
3. 💳 Card
👉 Enter payment method: 3

🧾 FINAL BILL
======================================================================
🆔 Order ID       : TB1004
👤 Customer Name  : Adithyan
📞 Phone Number   : 2299001122
🍽️ Order Type     : Takeaway
💳 Payment Method : Card
----------------------------------------------------------------------
Item                     Qty     Price       Total
----------------------------------------------------------------------
Ice Cream                1       ₹90         ₹90
----------------------------------------------------------------------
💰 Subtotal                                      ₹90.00
🎁 Discount                                        ₹0.00
🧾 GST (5%)                                        ₹4.50
----------------------------------------------------------------------
💵 FINAL AMOUNT                                   ₹94.50
======================================================================

💾 Complete order saved to order_history.txt

🎉 ORDER CONFIRMED!
🆔 Your Order ID: TB1004
💳 Payment Method: Card
💾 Order saved successfully.
🙏 Thank you for ordering from Tasty Bites!


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 8
➡️ Entered Choice: 8 - View Order History

📋 ORDER HISTORY
============================================================
[All previously saved orders will be displayed here]
============================================================


1. 📋 View Menu
2. 🛒 Add Items to Cart
3. 👀 View Cart
4. ✏️  Update Cart
5. 🗑️  Remove Item
6. 🧹 Clear Cart
7. 🧾 Place Order & Generate Bill
8. 📜 View Order History
9. 🔍 Search Order
10. 🏪 Restaurant Information
11. 🎁 Special Offers
12. ❌ Exit
==================================================
👉 Enter your choice: 12
➡️ Entered Choice: 12 - Exit

🙏 Thank you for visiting Tasty Bites!
👋 Have a great day!
