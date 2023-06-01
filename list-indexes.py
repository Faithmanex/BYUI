# # Shopping Cart Program

# # Create an empty list to store the names of the items in the shopping cart
# shopping_cart = []

# # Menu system that repeats until the user chooses to quit
# while True:
#     print("\nWelcome to the Shopping Cart Program!")
#     print("Please select one of the following:")
#     print("1. Add item")
#     print("2. View cart")
#     print("3. Remove item")
#     print("4. Compute total")
#     print("5. Quit")
    
#     # Get user's choice
#     choice = input("Please enter an action: ")
    
#     # Option 1: Add item
#     if choice == '1':
#         item = input("What item would you like to add? ")
#         shopping_cart.append(item)
#         print(f"'{item}' has been added to the cart.")
    
#     # Option 2: View cart
#     elif choice == '2':
#         print("The contents of the shopping cart are:")
#         for i, item in enumerate(shopping_cart, start=1):
#             print(f"{i}. {item}")
    
#     # Option 3: Remove item
#     elif choice == '3':
#         item_number = input("Which item would you like to remove? ")
#         try:
#             item_number = int(item_number)
#             if 1 <= item_number <= len(shopping_cart):
#                 item_removed = shopping_cart.pop(item_number - 1)
#                 print("Item removed.")
#             else:
#                 print("Sorry, that is not a valid item number.")
#         except ValueError:
#             print("Invalid input. Please enter a valid item number.")
    
#     # Option 4: Compute total
#     elif choice == '4':
#         # Placeholder for total computation
#         print("Computing the total...")
    
#     # Option 5: Quit
#     elif choice == '5':
#         print("Thank you. Goodbye.")
#         break
    
#     # Invalid choice
#     else:
#         print("Invalid choice. Please enter a valid action number.")


cart = []
item = ''
index = 0
list = ''
print('Please enter the items of the shopping list (type: quit to finish): ')

while item != 'quit':
    item = input('Item: ')
    if item != 'quit':
        cart.append(item)
print()


print('The shopping list is: ')
for i in cart:
    print(i)
print()


print('The shopping list with indexes is: ')
for i in range (len((cart))):
    index = i + 1
    list = cart[i]
    print(f'{index}. {list}')


element = int(input('Which element would you like to change? '))
new_item = input('What is the new Item? ')
cart[element - 1] = new_item

print('The shopping list with indexes is: ')
for i in range (len((cart))):
    index = i + 1
    list = cart[i]
    print(f'{index}. {list}')
