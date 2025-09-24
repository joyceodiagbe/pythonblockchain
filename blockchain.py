blockchain = [0]


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount):
    blockchain.append([get_last_blockchain_value(), transaction_amount])
    
    
add_value(10.1)
add_value(20.2)  # Call the function twice with different arguments
add_value(30.3)

print(blockchain)
   