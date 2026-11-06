
# CodeAlpha Python Programming Internship
# Task 2: Stock Portfolio Tracker

import csv

# STEP 1: Create a dictionary to store stock names and their prices.
# The stock name is the KEY and its price is the VALUE.
# These are manually defined sample prices, not live market prices.

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 170
}

# STEP 2: Create an empty list to store the user's portfolio details.
# Each stock's name, price, quantity and investment will be stored here.

portfolio = []

# This variable stores the total investment of all selected stocks.
total_investment = 0

# STEP 3: Display the program heading.

print("=" * 40)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 40)

# STEP 4: Display all available stocks and their prices.
# .items() gives us both the stock name and its price.

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# STEP 5: Take stock details from the user.
# The while loop allows the user to enter multiple stocks.
# The loop continues until the user enters "done".

while True:

    # Ask the user to enter a stock name.
    # upper() converts input into uppercase.
    # strip() removes unnecessary spaces.

    stock_name = input(
        "\nEnter stock name (or 'done' to finish): "
    ).upper().strip()

    # If the user enters "done", stop taking input.

    if stock_name == "DONE":
        break

    # Check whether the entered stock exists in our dictionary.
    # If it does not exist, show an error and ask again.

    if stock_name not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    # STEP 6: Ask for the quantity of shares.
    # try-except prevents the program from crashing
    # if the user enters text instead of a number.

    try:
        quantity = int(input("Enter quantity: "))

        # Quantity must be greater than zero.

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    # STEP 7: Calculate the investment for the selected stock.
    # Get the stock price from the dictionary.
    # Formula: Stock Price x Quantity

    price = stock_prices[stock_name]

    investment = price * quantity

    # Add this stock's investment to the total amount.

    total_investment += investment

    # STEP 8: Store the stock details in the portfolio list.
    # Each entry contains stock name, price, quantity and investment.

    portfolio.append([
        stock_name,
        price,
        quantity,
        investment
    ])

    print(f"Added {quantity} shares of {stock_name}.")

# STEP 9: Display the final portfolio.

print("\n" + "=" * 50)
print("             YOUR PORTFOLIO")
print("=" * 50)

# Display column headings.

print(f"{'Stock':<10}{'Price':<10}{'Quantity':<10}{'Value'}")

# Use a for loop to display every stock stored in the portfolio.

for item in portfolio:

    print(
        f"{item[0]:<10}"
        f"${item[1]:<9}"
        f"{item[2]:<10}"
        f"${item[3]}"
    )

# Display the total investment amount.

print("-" * 50)
print(f"Total Investment: ${total_investment}")

# STEP 10: Save the portfolio details in a CSV file.
# A CSV file stores data in rows and columns.
# Save only if the user has added at least one stock.

if portfolio:

    # Open portfolio.csv in write mode.
    # newline="" prevents extra blank lines in the CSV file.

    with open("portfolio.csv", "w", newline="") as file:

        # Create a CSV writer object to write data into the file.

        writer = csv.writer(file)

        # Write column headings in the first row.

        writer.writerow([
            "Stock Name",
            "Price",
            "Quantity",
            "Investment"
        ])

        # Write all portfolio records into the CSV file.

        writer.writerows(portfolio)

        # Write the final total investment.

        writer.writerow(["", "", "Total", total_investment])

    print("\nPortfolio saved successfully in portfolio.csv!")

else:
    print("\nNo stocks were added to your portfolio.")

# STEP 11: Display the closing message.

print("\nThank you for using Stock Portfolio Tracker!")
