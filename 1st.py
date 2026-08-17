  #   
#msg = input("enter your message?:")
#print(msg.lower())
#print(msg.find('bad'))
#print(msg.replace('bad' , '****'))
#note = "have been standing at edge of water long as remember never really knowing why"
#print(note , len(note))
#print(10+2)
#print(1-2)
#print(10/3)
#print(10//3)
#print(10%3)
#print(10*3)
#print(10**4)
#x=3
#x=x+7
#print(x)
#a = 5
#a = 10 + a
##a += 10
#print(a)
#import math
#print(math.ceil(3.8))
#print(math.floor(3.8))
#x = 3.7
#print(round(x))
#print(abs(-1.3))
#weight = int(input("enter your weight in kg"))
#height = float(input("enter your height in centimeter"))
#height = height / 100
#bmi = weight/ height **2
#print(bmi)

#weather = input("what's the weather outside: hot/cold ").lower()
#is_hot = True
#is_cold = False
#if weather == "hot":
#    print("it's a hot day")
#    print("drink plenty water")

#elif weather == "cold":
#    print("it's cold day")
#    print("wear warm clothes")

#else:
#    print("it's a lovely day")

#print("enjoy your day")

 
 
  
weight = int(input("enter your weight in Lbs: "))
height =float(input("enter your height t in meter: "))
weight_Lbs = 0.454 * weight 
bmi = weight_Lbs / height**2
print(bmi)


house_price = 1000000
good_credit = input("Do you have good credit? (yes/no): ").lower()
if good_credit == "yes":
    down_payment = house_price * 0.10
    print("You need to put down 10%")
elif good_credit == "no":
    down_payment = house_price * 0.20
    print("You need to put down 20%")

print("The down payment is ", down_payment)

    
Age = int(input("What is your age? "))
years_left = 100 - Age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12
print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")

    