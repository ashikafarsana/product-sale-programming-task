def calculate_discounted_price(quantity, price, discount_rate):
    if quantity > 30:
        discounted_price = 15 * price + (quantity - 15) * price * (1 - discount_rate)
    else:
        discounted_price = quantity * price
    return discounted_price


def calculate_discounted_total(quantity_dict, price_dict):
    total_quantity = sum(quantity_dict.values())
    total_amount = 0

    if total_quantity > 30:
        max_quantity = max(quantity_dict.values())
        if max_quantity > 15:
            discount_amount = calculate_discounted_price(max_quantity - 15, price_dict[max(quantity_dict, key=quantity_dict.get)], 0.5)
            total_amount += discount_amount
    for product, quantity in quantity_dict.items():
        price = price_dict[product]
        if quantity > 10:
            discount_amount = calculate_discounted_price(quantity, price, 0.05)
            total_amount += discount_amount
        else:
            total_amount = quantity * price
        if quantity >20:
            discount_name = "bulk_10_discount"
            discount_amount = calculate_discounted_price(quantity, price, 0.10)
            total_amount += discount_amount
        else:
            total_amount = quantity * price
        if quantity >30:
            discount_name = "tiered_50_discount"
            discount_amount = discounted_price
            total_amount +=  discount_amount
        else:
            total_amount = quantity * price

            
            
    return total_amount


def calculate_shipping_fee(quantity_dict):
    total_quantity = sum(quantity_dict.values())
    shipping_fee = (total_quantity // 10) * 5
    return shipping_fee


def calculate_gift_wrap_fee(quantity_dict):
    total_quantity = sum(quantity_dict.values())
    return total_quantity


def main():
    # Product catalog
    products = {
        "Product A": 20,
        "Product B": 40,
        "Product C": 50
    }

    # Input quantities and gift wrap information
    quantity_dict = {}
    gift_wrap_dict = {}
    

    for product, price in products.items():
        quantity = int(input(f"Enter the quantity of {product}: "))
        gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ")
        quantity_dict[product] = quantity
        gift_wrap_dict[product] = gift_wrap.lower() == "yes"

    # Calculate subtotal
    subtotal = sum(quantity * products[product] for product, quantity in quantity_dict.items())

    # Calculate discount
    discount_name = ""
    discount_amount = 0
    total_amount = 0

    if subtotal > 200:
        discount_name = "flat_10_discount"
        discount_amount = 10
        total_amount = subtotal - discount_amount
    else:
        total_amount = subtotal
    
        if quantity >20:
            discount_name = "bulk_10_discount"
            discount_amount = calculate_discounted_price(quantity, price, 0.10)
            total_amount += discount_amount
        else:
            total_amount = subtotal
        if quantity >30:
            discount_name = "tiered_50_discount"
            discount_amount = discounted_price
            total_amount =  discount_amount
        else:
            total_amount = subtotal

    
    total_amount -= calculate_discounted_total(quantity_dict, products)

    # Calculate shipping fee
    shipping_fee = calculate_shipping_fee(quantity_dict)

    # Calculate gift wrap fee
    gift_wrap_fee = calculate_gift_wrap_fee(gift_wrap_dict)

    # Calculate total
    total = total_amount + shipping_fee + gift_wrap_fee

    # Output details
    print("\n----- Order Summary -----")
    for product, quantity in quantity_dict.items():
        amount = quantity * products[product]
        print(f"{product}: Quantity: {quantity}, Amount: ${amount}")
    print(f"\nSubtotal: ${subtotal}")
    if discount_name:
        print(f"{discount_name}: Discount Amount: ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"Total: ${total}")



main()