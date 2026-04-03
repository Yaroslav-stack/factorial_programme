import math

active = True
while active:

    print("\nWelcome to proggramm!\n")
    try:
        message_1 = int(input("Enter n number: "))
        message_2 = int(input("Enter k number: "))
        if message_2 > message_1:
            print("Error! k number can't be more than n")
        else:
            num_of_acc = math.factorial(message_1)/math.factorial(message_1 - message_2)
        num_of_comb = math.factorial(message_1)/math.factorial(message_2)/ \
          math.factorial(message_1 - message_2)
        
        print(f"\nNumber of accomodations: {num_of_acc}")
        print(f"Number of combinations: {num_of_comb}")
    except ValueError:
        print("Error! Space can only contain numbers")

    while True:
        message_continue = input("\nDo you want to continue? (yes/no): ").lower()
        if message_continue == 'no':
            print("Thanks for using program!")
            active = False
            break
        elif message_continue == 'yes':
            active = True
            break
        else:
            print("Error! Please enter only 'yes' or 'no'")
