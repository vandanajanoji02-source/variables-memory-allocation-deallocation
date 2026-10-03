def calculate_discount(purchase_amount):
    if purchase_amount >= 5000:
        discount_rate = 0.20
    elif purchase_amount >= 3000:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = purchase_amount * discount_rate
    final_payable_amount = purchase_amount - discount_amount
    return discount_amount, final_payable_amount


if __name__ == "__main__":
    discount, payable = calculate_discount(4000)
    print("Discount amount:", discount)
    print("Final payable amount:", payable)