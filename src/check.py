def add(a,b):
    return a + b

def dev(a,b):
    return a - b


def calculate_subtotal(items):
    """Calculate total price before discount."""
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    return total


def calculate_discount(subtotal, customer_type):
    """Calculate discount based on customer type."""

    if customer_type == "premium":
        return subtotal * 0.20

    elif customer_type == "regular":
        return subtotal * 0.10

    return 0


def calculate_final_price(items, customer_type):
    """Calculate final price after applying discount."""
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal, customer_type)

    return subtotal + discount


def apply_tax(price, tax_rate):
    """Apply tax to the price."""
    return price * (1 + tax_rate)


def checkout(items, customer_type, tax_rate):
    """Calculate final checkout price."""

    subtotal = calculate_subtotal(items)
    final_price = calculate_final_price(items, customer_type)

    return apply_tax(final_price, tax_rate)




a = [1,2,3]
b = [1,3,4]




                


