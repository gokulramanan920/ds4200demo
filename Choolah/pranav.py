"""
Gokul Ramanan
9/18/25
DS 4200
"""

def get_choolah_credit(*item):
    choolah_prices = {"bowl": 11.99, "wrap": 10.49, "lassi": 5.75, "samosa": 4.99, "paneer": 2.49, "sprite": 1.99}
    total_choolah = 0
    for items in item:
        if items.lower() in choolah_prices.keys():
            total_choolah += choolah_prices[items.lower()]
    return round(total_choolah, 2)

choolah_bill = get_choolah_credit("Bowl", "LASSI", "samosa")
print(f"The total Choolah bill today is: ${choolah_bill}")
