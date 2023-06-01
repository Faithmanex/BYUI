cart = []
item = ''
index = 0
list = ''
selection = 0

print('Welcome to the Shopping Cart Program! ')

while selection != 5:
    print('Please select ont of the following: ')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    selection = int(input('Please enter an action: '))
    if selection == 1:
        item = input('What item would you like to add? ')
        cart.append(item)
    elif selection == 2:
        print('The contents of the shopping cart are: ')
        for i in range (len((cart))):
            index = i + 1
            list = cart[i]
            print(f'{index}. {list}')
    elif selection == 3:
        print()
    elif selection == 4:
        print()
    elif selection == 5:
        print()



# print('Please enter the items of the shopping list (type: quit to finish): ')




# while item != 'quit':
#     item = input('Item: ')
#     if item != 'quit':
#         cart.append(item)
# print()


# print('The shopping list is: ')
# for i in cart:
#     print(i)
# print()


# print('The shopping list with indexes is: ')
# for i in range (len((cart))):
#     index = i + 1
#     list = cart[i]
#     print(f'{index}. {list}')


# element = int(input('Which element would you like to change? '))
# new_item = input('What is the new Item? ')
# cart[element - 1] = new_item

# print('The shopping list with indexes is: ')
# for i in range (len((cart))):
#     index = i + 1
#     list = cart[i]
#     print(f'{index}. {list}')
