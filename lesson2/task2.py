import json


def write_order_to_json(item, quantity, price, buyer, date):
    spam = {"item": item,
            "quantity": quantity,
            "price": price,
            "buyer": buyer,
            "date": date
            }
    with open('orders.json', 'w') as f:
        json.dump(spam, f, indent=4)


write_order_to_json(1, 2, 3, 4, 5)
