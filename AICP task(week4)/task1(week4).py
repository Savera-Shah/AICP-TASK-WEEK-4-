class Item:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.num_bids = 0

    def display_info(self):
        print(f"Item Number: {self.item_number}")
        print(f"Description: {self.description}")
        print(f"Reserve Price: ${self.reserve_price}")
        print(f"Number of Bids: {self.num_bids}")


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


def validate_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def setup_auction():
    print("Welcome to the auction setup.")
    num_items = validate_integer("Enter the number of items in the auction (should be at least 10): ")
    while num_items < 10:
        print("There must be at least 10 items in the auction.")
        num_items = validate_integer("Enter the number of items in the auction (should be at least 10): ")

    items = []
    for i in range(num_items):
        print(f"\nSetting up item {i+1}:")
        item_number = input("Enter item number: ")
        description = input("Enter item description: ")
        reserve_price = validate_positive_float("Enter reserve price: $")
        items.append(Item(item_number, description, reserve_price))
    
    print("\nAuction setup complete. Details of items:")
    for item in items:
        item.display_info()


if __name__ == "__main__":
    setup_auction()
