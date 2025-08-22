# Stock Portfolio Tracker

# Hardcoded stock prices (in USD)
stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 2800,
        "MSFT": 310,
        "AMZN": 130
}

portfolio = {}

# Take user input for stocks and quantity
while True:
        stock = input("Enter stock symbol (AAPL, TSLA, GOOG, MSFT, AMZN) or 'done' to finish: ").upper()
        if stock == "DONE":
                break
        if stock not in stock_prices:
                print("Stock not available in our list. Try again.")
                continue
        qty = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty

# Calculate total investment
total_value = 0
print("\nPortfolio Summary:")
for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        total_value += value
        print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optionally save results in a text file
save = input("\nDo you want to save the result to 'portfolio.txt'? (yes/no): ").lower()
if save == "yes":
        with open("portfolio.txt", "w") as f:
                f.write("Portfolio Summary:\n")
                for stock, qty in portfolio.items():
                        f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
                f.write(f"\nTotal Investment Value: ${total_value}\n")
        print("Portfolio saved to 'portfolio.txt'")

