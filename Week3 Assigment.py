def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it's 20% or more."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price  # Return original price if discount is less than 20%

# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the result
print(f"Final price: ${final_price:.2f}")