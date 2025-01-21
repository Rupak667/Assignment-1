def main():
    grocery_list = []

    while True:
        choice = input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?: ")

        if choice == '1':
            item = input("What will be added?: ")
            grocery_list.append(item)
        elif choice == '2':
            if grocery_list:
                print(f"There are {len(grocery_list)} items in the list.")
                try:
                    item_index = int(input("Which item is deleted?: "))
                    if 0 <= item_index < len(grocery_list):
                        grocery_list.pop(item_index)
                    else:
                        print("Incorrect selection.")
                except ValueError:
                    print("Incorrect selection.")
            else:
                print("The list is empty.")
        elif choice == '3':
            print("The following items remain in the list:")
            for item in grocery_list:
                print(item)
            break
        else:
            print("Incorrect selection.")

if __name__ == "__main__":grossary-2.py
    main()
