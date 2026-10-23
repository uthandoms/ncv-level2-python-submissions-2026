def place_order(item):
    
    print(f"Order placed: your order is {item}")
    
   
def calculate_total(item):
    baseprice = 25.5
    vat = 0.15
    totalPrice = (baseprice + len(item)) * 1.15
    
    return totalPrice
    
def get_order():
    print("Preparing Order")
    return("order ready")

myfood = input("What would you like")
place_order(myfood)

print(get_order())

order_total = calculate_total(myfood)
print(f"Your order cost:R {order_total}")

