print("===========================================================================")
print(f"{'Temperature Converter':^60}")
print("===========================================================================")
print("""

""")

#تاریخچه
History=[]

#سلسیوس به فارنهایت
def celsius_to_fahrenheit(celcious):
    result=(celcious*1.8)+32
    History.append(f"{'celcious degree:  ',celcious},{' = '},{"Fahrenheit ",result}")
    return result

#فارنهایت به سلسیوس
def fahrenheit_to_celsius(fahrenheit):
    result=(fahrenheit-32)/1.8
    History.append(f"{'Fahrenheit degree: ',fahrenheit},{' = '},{'Celcious ',result}")
    return result

#سلسیوس به کالوین
def celsius_to_kalvin(celcious):
    result=celcious+273.15
    History.append(f"{'Celcious degree: ',celcious},{' = '}, {'Kalvin ',result}")
    return result

#کالوین به سلسیوس 
def kalvin_to_celsius(kalvin):
    result=kalvin-273.15
    History.append(f"{'Kalvin degree: ',kalvin},{' = '},{'Celcious ',result}")
    return result


while True:
    print("""
    1. Celsius to Fahrenheit
    2. Fagrenheit to celsius
    3. Celcius to kelvin
    4. kelvin to Celsius
    5. Show History
    6. Exit
        """)
    try:
        user_menu=int(input("Please Choose on action below:    "))
    except ValueError:
        print("Please choose one number!  ")
        continue
    
    if user_menu==1:
        print(celsius_to_fahrenheit(float(input("Enter the celcious degree:    "))))
    elif user_menu==2:
        print(fahrenheit_to_celsius(float(input("Enter the Fahrenheit degree:   "))))
    elif user_menu==3:
        print(celsius_to_kalvin(float(input("Enter the celsius degree:    "))))
    elif user_menu==4:
        print(kalvin_to_celsius(float(input("Enter the kalvin degree:    "))))
    elif user_menu==5:
        if not History:
            print("History is empty! ")
        else:
            for item in History:
                print(item)
    elif user_menu==6:
        print("Have a nice Time Dude😊")
        break
        


        
    

