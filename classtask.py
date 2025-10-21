class Mobile:
    # Class-level attribute
    company = "DefaultCompany"

    def __init__(self, price, made_in, battery):
        # Instance attributes
        self.price = price
        self.made_in = made_in
        self.battery = battery

    def display(self):
        print("MOBILE COMPANY:", self.company)  # Will show class-level company
        print("MOBILE PRICE:", self.price)
        print("MOBILE BATTERY:", self.battery)
        print("MOBILE MADE IN:", self.made_in)

    @classmethod
    def change_company_name(cls, new_name):
        cls.company = new_name  # Updates the class-level attribute

    @staticmethod
    def new_update():
        print("Phone Update changed")


# Example usage
mob1 = Mobile(100000, "America", "9000mah")
mob2 = Mobile(50000, "India", "7000mah")

# Display original
mob1.display()
mob2.display()
print()

# Change company name for all instances
Mobile.change_company_name("Moto")

# Display after change
mob1.display()
mob2.display()
print()

# Static method call
mob1.new_update()
mob2.new_update()
