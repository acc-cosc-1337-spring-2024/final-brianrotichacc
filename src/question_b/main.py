import question_b as b
def display_menu():
    print(" Option 1: Display stock purchase history\n Option 2: Exit ")

display_menu()
while True:
    choose_value = int(input("Please enter your option: "))
    if choose_value == 1:
        b.stock_purchase_history()
    elif choose_value ==2:
        exit()
    else:
        print("Please enter a valid choice")
        pass
    keep_going = input("Do you want to continue? (Y/N): ").lower()
    if keep_going != 'y':
        exit()