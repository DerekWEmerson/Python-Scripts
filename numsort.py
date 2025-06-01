# After saying "no" to values are correct, make sure to verify again.

numlist = []

def main():
    amount = amount_to_sort()
    add_num(amount)
    verify = verify_list(numlist)
    if verify == 2:
        numlist.clear()
        add_num(amount)
    which_sort(numlist)
    print(numlist)

def amount_to_sort():
    amount = int(input("Amount of values to sort: "))
    return amount
    
def add_num(num_of_values):
    x = int(num_of_values) + 1
    for i in range(1, x):
        while True:
            num = input(f"Value {i}: ")
            try:
                num = float(num)
                numlist.append(num)
                break
            except ValueError:
                print("Please type a number.")

def verify_list(numlist):
    while True:
        verify = input(
        f"{numlist} \n"
        "Are these values correct? y or n: "
        )
        if verify.lower() == "y":
            return 1
        elif verify.lower() == "n":
            return 2
        else:
            print("Please type 'y' or 'n'.")

def which_sort(numlist):
    while True:
        sort = input(
        "1. Highest to Lowest \n" 
        "2. Lowest to Highest \n"
        "Choose an option: "
        )
        if sort == "1":
            return sort_high_to_low(numlist)
        elif sort == "2":
            return sort_low_to_high(numlist)
        else:
            print("Please type 1 or 2.")

def sort_high_to_low(numlist):
    numlist.sort(reverse=True)
    return numlist

def sort_low_to_high(numlist):
    numlist.sort()
    return numlist

if __name__ == "__main__":
    main()