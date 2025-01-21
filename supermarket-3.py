def main():
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total_sum = 0

    print("Supermarket\n===========")
    while True:
        product = int(input("Please select product (1-10) 0 to Quit: "))
        if product == 0:
            break
        elif 1 <= product <= 10:
            print(f"Product: {product} Price: {prices[product - 1]}")
            total_sum += prices[product - 1]
        else:
            print("Incorrect selection.")

    print(f"Total: {total_sum}")
    payment = float(input("Payment: "))
    change = payment - total_sum
    print(f"Change: {change}")


if __name__ == "__main__":
    main()
