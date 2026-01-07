import json

data = []

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Input data')
    print('2: Output data')
    print('q: Quit')
    choice = input('Your choice: ')
    if choice == '1':
        user_input = input('Enter Something: ')
        data.append(user_input)

        with open('blockchain.txt', mode='w') as f:
            f.write(json.dumps(data))
            f.write('\n')
    elif choice == '2':
        print(data)
    elif choice == 'q':
        waiting_for_input = False
    else:
        print("Invalid choice")