#write functions here, don't add input('') statements here!
def numbers():
    numbers = []

    for i in range(5):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid number.")

    lowest_number = min(numbers)
    highest_number = max(numbers)
    total = sum(numbers)
    average = total/len(numbers)
    # Display the results
    print("\nResults:")
    print(f"The lowest number in the list: {lowest_number}")
    print(f"The highest number in the list: {highest_number}")
    print(f"The total of the numbers in the list: {total}")
    print(f"The average of the numbers in the list: {average}")
