blockchain= [0]

#def add_value():
#    blockchain.append([blockchain[0], 5.3])
#    print(blockchain)

#add_value() 
#add_value() # Call the function twice

# Function receive arguments
def add_value2(transaction_amount):
    blockchain.append([blockchain[-1], transaction_amount])
    print(blockchain)

    add_value2(10.1)
    add_value2(20.2) # Call the function twice with different arguments
    add_value2(30.3)