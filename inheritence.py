class Mobile:
    mobile_type = "Android"

    def __init__(self, company, price, made_in, battery):
        self.company = company
        self.price = price
        self.made_in = made_in
        self.battery = battery
        print("MOBILE COMPANY:", self.company)
        print("MOBILE PRICE:", self.price)
        print("MOBILE BATTERY:", self.battery)
        print("MOBILE MADE IN:", self.made_in)

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

    def storage(self):
        print("Storage of mobile is", self.storagemobile)


class UpdateMobile(Mobile):
    def __init__(self, company, price, made_in, battery, storage):
        super().__init__(company, price, made_in, battery)
        self.storagemobile = storage
        print("MOBILE STORAGE:", self.storagemobile)

    # ✅ Properly overridden display method
    def display(self):
        super().display()
        print("MOBILE STORAGE:", self.storagemobile)


# ---------- Object creation and usage ----------
mob = Mobile("apple", 100000, "America", "9000mah")
mob.company = "Vivo"
print(mob.company)
mob.price = 10000
print(mob.price)
mob.made_in = "India"
print(mob.made_in)
mob.battery = "7000mah"
print(mob.battery)

mob.display()
mob.new_update()
mob.change_company_name("Moto")
print(mob.newcompany)

# add dynamic storage property
mob.storagemobile = "128GB"
mob.storage()
mob.newspace = "328GB"

print("\n--- Inherited Class (Single Inheritance) ---")
mob1 = UpdateMobile("vivonew", 15000, "China", "4000mah", "128GB")
mob1.display()
