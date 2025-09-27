# # Initializing our (empty) blockchain list
# blockchain = [0]


# def get_last_blockchain_value():
#     """ Returns the last value of the current blockchain. """
#     if len(blockchain) < 1:
#         return None
#     return blockchain[-1]

# # This function accepts two arguments.
# # One required one (transaction_amount) and one optional one (last_transaction)
# # The optional one is optional because it has a default value => [1]


# def add_transaction(transaction_amount, last_transaction=[1]):
#     """ Append a new value as well as the last blockchain value to the blockchain.

#     Arguments:
#         :transaction_amount: The amount that should be added.
#         :last_transaction: The last blockchain transaction (default [1]).
#     """
#     if last_transaction is None:
#         last_transaction = [1]
#     blockchain.append([last_transaction, transaction_amount])


# def get_transaction_value():
#     """ Returns the input of the user (a new transaction amount) as a float. """
#     # Get the user input, transform it from a string to a float and store it in user_input
#     user_input = float(input('Your transaction amount please: '))
#     return user_input


# def get_user_choice():
#     """ Returns the input of the user (a new transaction amount) as a float. """
#     # Get the user input, transform it from a string to a float and store it in user_input
#     user_input = input('Your choice: ')
#     return user_input


# def print_blockchain_elements():
#     for block in blockchain:
#         print('Outputting block')
#         print(block)
#     else:
#         print('-' * 20)


# def verify_chain():
#     """ Verify the current blockchain and return True if it's valid, False if it's not. """
#     # block_index = 0
#     is_valid = True
#     for block_index in range(len(blockchain)):
#        if block_index == 0:
#            continue
#        elif blockchain[block_index][0] == blockchain[block_index - 1]:
#            is_valid = True
#        else:
#            is_valid = False
#            break
#     # for block in blockchain:
#     #     if block_index == 0:
#     #         block_index += 1
#     #         continue
#     #     elif block[0] == blockchain[block_index - 1]:
#     #         is_valid = True
#     #     else:
#     #         is_valid = False
#     #         break
#     #     block_index += 1
#     return is_valid


# waiting_for_input = True


# while waiting_for_input:
#     print('Please choose')
#     print('1: Add a new transaction value')
#     print('2: Output the blockchain blocks')
#     print('h: Manipulate the chain')
#     print('q: Quit')
#     user_choice = get_user_choice()
#     if user_choice == '1':
#         tx_amount = get_transaction_value()
#         add_transaction(tx_amount, get_last_blockchain_value())
#     elif user_choice == '2':
#         print_blockchain_elements()
#     elif user_choice == 'h':
#         if len(blockchain) >= 1:
#             blockchain[0] = [2]
#     elif user_choice == 'q':
#         waiting_for_input = False
#     else:
#         print('Invalid choice, please pick either 1 or 2')
#     if not verify_chain():
#         print('Invalid blockchain!')
#         break
# else:
#     print('User left!')

# print('Done!')

# Assignment
# 1) Create a list of names and use a for loop to output the length of each name (len()).
# 2) Add an if check inside the loop to only output names longer than 5 characters.
# 3) Add another if check to see whether a name includes a “n” or “N” character.
# 4) Use a while loop to empty the list of names (via pop())
names = ['Max', 'Monika', 'Moritz']
for name in names:
    print(f'{name} is {len(name)} characters long.')
    if len(name) > 5:
        print(f'{name} has more than 5 characters!')
        continue
    if 'n' in name or 'N' in name:
        print(f'The letter n is in {name}.')

# Use a while  loop to empty the list of names (via pop()).
while names:
    names.pop()
    print(names)
