auto = 20
bike = 40
car = 50
wrap_auto=0
wrap_bike=0
wrap_car=0
def giftwrap():
    gift_wrap = input("Do you want the product wrapped as a gift (yes/no)")
    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']
    if gift_wrap.lower() in yes_choices:
        return 1
    elif gift_wrap.lower() in no_choices:
        return 0
auto_amount = int(input("How much auto do you want ?"))
if auto_amount > 0:
    wrap_auto = giftwrap()
bike_amount = int(input("How much bike do you want ?"))
if bike_amount > 0:
    wrap_bike = giftwrap()
car_amount = int(input("How much car do you want ?"))
if car_amount > 0:
    wrap_car = giftwrap()
if auto_amount > 0:
    print("You have orderd",auto_amount,"auto for :$", auto*auto_amount)
if bike_amount > 0:
    print("You have orderd",bike_amount,"bike for :$", bike*bike_amount)
if car_amount > 0:
    print("You have orderd",car_amount,"car for : $", car*car_amount)
total_amount = auto_amount + bike_amount + car_amount
subtotal = auto*auto_amount+bike*bike_amount+car*car_amount
print("subtotal for this purchase is : $",subtotal)
flat_10_discount = 0
bulk_5_discount = 0
bulk_10_discount = 0
tiered_50_discount = 0
discount_1 = 0
discount_2 = 0
discount_3 = 0
discount_4 = 0
if subtotal > 200:
    discount_1 = 10
    flat_10_discount = subtotal - discount_1
if auto_amount >10 or car_amount > 10 or bike_amount > 10:
    if auto_amount > 10:
        discount_2 = (auto_amount*auto*5)/100
    elif bike_amount > 10:
        discount_2 = (bike_amount*bike*5)/100
    elif car_amount > 10:
        discount_2 = (car_amount*car*5)/100
bulk_5_discount = subtotal - discount_2
if auto_amount + bike_amount + car_amount > 20:
    discount_3 = (subtotal * 10) / 100
    bulk_10_discount = subtotal - discount_3

if (auto_amount + bike_amount + car_amount > 30) and ( auto_amount > 15 or bike_amount > 15 or car > 15 ):
    if auto_amount > 15 :
        discount_4 = ( auto_amount * auto * 50 ) / 100
    elif bike_amount > 15 :
        discount_4 = ( bike_amount * bike * 50 ) / 100
    elif car_amount > 15 :
        discount_4 = ( car_amount * car * 50 ) / 100
    tiered_50_discount = subtotal - discount_4
final_discount = [ discount_1 , discount_2 , discount_3 , discount_4 ]
final_discount.sort()
discount_flag=0
if final_discount[3] == discount_1:
    discount_flag=1
    print("flat_10_discount is applied. The discount amount is : $", discount_1)
elif final_discount[3] == discount_2:
    discount_flag=2
    print("bulk_5_discount is applied. The discount amount is : $", discount_2)
elif final_discount[3] == discount_3:
    discount_flag=3
    print("bulk_10_discount is applied. The discount amount is : $", discount_3)
elif final_discount[3] == discount_4:
    discount_flag=4
    print("tiered_50_discount is applied. The discount amount is : $", discount_4)
if discount_flag == 1:
    total = flat_10_discount 
elif discount_flag == 2:
    total = bulk_5_discount 
elif discount_flag == 3:
    total = bulk_10_discount 
elif discount_flag == 4:
    total = tiered_50_discount 
else: 
    total = subtotal
total_gift_wrap_fee = 0
if wrap_auto == 1:
    total=total + auto_amount
    total_gift_wrap_fee = total_gift_wrap_fee + auto_amount
    print("Gift wrap fee for auto : $", auto_amount)
if wrap_bike == 1:
    total=total + bike_amount
    total_gift_wrap_fee = total_gift_wrap_fee + bike_amount
    print("Gift wrap fee for bike : $", bike_amount)
if wrap_car == 1:
    total=total + car_amount
    total_gift_wrap_fee = total_gift_wrap_fee + car_amount
    print("Gift wrap fee for car : $", car_amount)
if wrap_car == 1 or wrap_bike == 1 or wrap_auto == 1:
    print("total gift wrap fee is : $", total_gift_wrap_fee)
if total_amount%10 == 0:
    package_quantity = int( ( total_amount / 10 ))
    print("The shipping fee for your purchase : $", package_quantity * 5) 
else:
    package_quantity = int( ( total_amount / 10 ) +1)
    print("The shipping fee for your purchase : $", package_quantity * 5)
shipping_fee = package_quantity * 5
total = total + shipping_fee
print("Your total amount for this order is :", total)