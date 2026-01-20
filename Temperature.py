#convertiser celsuis
print("welcom to the convertiser ")
print("KELVIN(k)")
print("Fahrenheit (F)")
print("Celsius(C)")

def convertiser_c():


    if celsius<-273.15:
        print("impossible")
    elif choix!=1 and choix!=2:
        print("choice a number between(1,2)")

    elif choix==1:
        kelvin= celsius+ 273.15
        print(f"convertion of {celsius}°C celsius to kelvin {kelvin} ")
    elif choix==2:
        fahrenheit= (celsius *1.8) + 32
        print(f"convertion of {celsius}°C celsius to {fahrenheit}°F")


celsius = float(input("enter the temperature in celsius:"))
choix=int(input("choice 1=kelvin , 2=Fnahrenheit:"))
convertiser_c()

