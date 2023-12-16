class Table:
    def __init__(self, num_of_diners):
        if num_of_diners == 0:
            raise ValueError("Number of diners can't be zero.")
        self.num_of_diners = num_of_diners
        self.bill = []

    def order(self, item, price, quantity = 1):
        for items in self.bill:
            if items['item'] == item and items['price'] == price:
                items['quantity'] += quantity
                break
        else:
            self.bill.append({"item": item, "price": price, "quantity": quantity})

    def remove(self, item, price, quantity=1):
        for items in self.bill:
            if items['item'] == item and items['price'] == price:
                if items['quantity'] < quantity:
                    return False
                items['quantity'] -= quantity
                if items['quantity'] == 0:
                    self.bill.remove(items)
                break
        else:
            return False
        return True
    
    def get_subtotal(self):
        subtotal = 0
        for item in self.bill:
            subtotal += item['price'] * item['quantity']
        return subtotal

    def get_total(self, service_charge=0.10):
            subtotal = self.get_subtotal()
            service_charge_amount = subtotal * service_charge
            total = subtotal + service_charge_amount
            return {
                "Sub Total": f"£{subtotal:.2f}",
                "Service Charge": f"£{service_charge_amount:.2f}",
                "Total": f"£{total:.2f}"
            }
    
    def split_bill(self):
        if self.num_of_diners == 0:
            return "Error: Number of diners can't be zero."
        else:
            subtotal = self.get_subtotal()
            per_diner = subtotal / self.num_of_diners
            return round(per_diner, 2)