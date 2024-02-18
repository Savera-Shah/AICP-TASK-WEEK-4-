class Item:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.num_bids = 0
        self.highest_bid = 0

    def display_info(self):
        print(f"Item Number: {self.item_number}")
        print(f"Description: {self.description}")
        print(f"Current Highest Bid: ${self.highest_bid}")
        print(f"Number of Bids: {self.num_bids}")

    def place_bid(self, bid_amount):
        if bid_amount > self.highest_bid:
            self.highest_bid = bid_amount
            self.num_bids += 1
            print("Bid placed successfully.")
        else:
            print("Your bid must be higher than the current highest bid.")


def find_item(items, item_number):
    for item in items:
        if item.item_number == item_number:
            return item
    return None


def validate_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("Welcome to the auction!")
    num_items = int(input("Enter the number of items in the auction: "))

    items = []
    for _ in range(num_items):
        item_number = input("Enter item number: ")
        description = input("Enter item description: ")
        reserve_price = validate_positive_float("Enter reserve price: $")
        items.append(Item(item_number, description, reserve_price))

    print("\nAuction setup complete. Let the bidding begin!")

    while True:
        print("\nOptions:")
        print("1. Place a bid")
        print("2. View item details")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item_number = input("Enter item number: ")
            item = find_item(items, item_number)
            if item:
                bid_amount = validate_positive_float("Enter your bid amount: $")
                item.place_bid(bid_amount)
            else:
                print("Item not found.")
        
        elif choice == "2":
            item_number = input("Enter item number: ")
            item = find_item(items, item_number)
            if item:
                item.display_info()
            else:
                print("Item not found.")

        elif choice == "3":
            print("Thank you for participating in the auction!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
