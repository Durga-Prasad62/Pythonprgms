class Mobile:
    def __init__(self, company, price, made_in, battery):
        self.company = company
        self.price = price
        self.made_in = made_in
        self.battery = battery

    def display(self):
        print("MOBILE COMPANY:", self.company)
        print("MOBILE PRICE:", self.price)
        print("MOBILE BATTERY:", self.battery)
        print("MOBILE MADE IN:", self.made_in)

    @classmethod
    def change_company_name(cls, new_name):
        cls.newcompany = new_name

    @staticmethod
    def new_update():
        print("Phone Update changed")

# Example usage
mob = Mobile("Apple", 100000, "America", "9000mah")
mob.company = "Vivo"
mob.price = 10000
mob.made_in = "India"
mob.battery = "7000mah"
mob.display()
mob.new_update()
mob.change_company_name("Moto")
print(mob.newcompany)

