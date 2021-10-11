import random

guests_number = int(input('Enter the number of friends joining (including you):\n'))
if guests_number <= 0:
    print('\nNo one is joining for the party')
else: 
    print('\nEnter the name of every friend (including you), each on a new line:\n')
    quests_names = [input() for _ in range(guests_number)]
    
    bill = float(input('\nEnter the total bill value:\n'))
    
    lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky == 'Yes':
        lucky_friend = random.choice(quests_names)
        print(f'\n{lucky_friend} is the lucky one!\n')
        split_value = round(bill / (guests_number - 1), 2)
        quests_dict = dict.fromkeys(quests_names, split_value)
        quests_dict[lucky_friend] = 0
    else:
        split_value = round(bill / guests_number, 2)
        print('\nNo one is going to be lucky\n')
        quests_dict = dict.fromkeys(quests_names, split_value)

    print(quests_dict)