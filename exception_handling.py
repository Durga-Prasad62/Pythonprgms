
# try:
#     print("Hello")
# must have a except or finally


try:
    print("Inside try block")
    x = 10 / 0   # error occurs here
finally:
    print("Finally block executed")


try:
    a = int(input("enter a num1"))
    b = int(input("enter a num2"))
    print(a/b)
except ValueError as e:
    print(e) 
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print(" handles the errors using exception")



try:
    a = int(input("enter a num1"))
    b = int(input("enter a num2"))
    print(a/b)
except (ValueError,ZeroDivisionError) as e:
    print(e) 
except Exception as e:
    print(e)
else:
    print("try is executed successfully")
finally:
    print(" handles the errors using exception")

# raise value error 
try:
    amount = float(input("Enter amount to pay: ₹"))
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    
    print("Processing payment...")
    
    payment_status = "success"   

except ValueError as e:
    print("Payment error:", e)

else:
    print("Payment completed successfully! Transaction status:", payment_status)

finally:
    print("Transaction closed. Thank you for using our service.")



class NegativeAgeError(Exception):
    pass

age = -5
if age < 0:
    raise NegativeAgeError("Custom: Age cannot be negative")




try:
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number for age.")
finally:
    print("User input handling complete.")


class Car():
    def car_name():
        print("this is a innova car")
    def car_color():
        print("this is the black color")
obj = Car()
print(obj.car_engine)  # attribute error