import question_d as d

def display_menu():
    print(" Option 1: Display Multiplication Table\n Option 2: Exit ")

display_menu()
while True:
    choose_value = int(input("Please enter your option: "))
    if choose_value == 1:
        table_list = d.create_multiplication_table()
        d.display_multiplication_table(table_list)
    elif choose_value == 2:
        exit()
    else:
        print("Please enter a valid choice")
    keep_going = input("Do you want to continue? (Y/N): ").lower()
    if keep_going != 'y':
        exit() 