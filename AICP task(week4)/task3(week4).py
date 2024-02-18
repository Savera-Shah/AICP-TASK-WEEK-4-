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
        print(f"Reserve Price: ${self.reserve_price}")
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


def calculate_fee(final_bid):
    return final_bid * 0.1


def main():
    print("Welcome to the auction!")
    num_items = int(input("Enter the number of items in the auction: "))

    items = []
    total_fee = 0
    items_sold = 0
    items_not_meeting_reserve = 0
    items_with_no_bids = []

    for _ in range(num_items):
        item_number = input("Enter item number: ")
        description = input("Enter item description: ")
        reserve_price = float(input("Enter reserve price: $"))
        items.append(Item(item_number, description, reserve_price))

    print("\nAuction setup complete. Let the bidding begin!")

    while True:
        print("\nOptions:")
        print("1. Place a bid")
        print("2. View item details")
        print("3. End auction")
        choice = input("Enter your choice: ")

        if choice == "1":
            item_number = input("Enter item number: ")
            item = find_item(items, item_number)
            if item:
                bid_amount = float(input("Enter your bid amount: $"))
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
            print("\nAuction ended. Results:")
            for item in items:
                if item.highest_bid >= item.reserve_price:
                    items_sold += 1
                    fee = calculate_fee(item.highest_bid)
                    total_fee += fee
                    print(f"Item {item.item_number} - Sold for ${item.highest_bid}. Auction fee: ${fee}")
                elif item.num_bids > 0:
                    print(f"Item {item.item_number} - Highest bid did not meet reserve price: ${item.highest_bid}")
                    items_not_meeting_reserve += 1
                else:
                    print(f"Item {item.item_number} - No bids received.")
                    items_with_no_bids.append(item.item_number)
            
            print("\nSummary:")
            print(f"Total Auction Fee: ${total_fee}")
            print(f"Number of Items Sold: {items_sold}")
            print(f"Number of Items Not Meeting Reserve: {items_not_meeting_reserve}")
            print(f"Number of Items with No Bids: {len(items_with_no_bids)}")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
