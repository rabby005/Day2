# if diye start hobe
# elif hove or 
# else diye ses hobe



#
age1 =16

if(age1 >= 18):
    print("Can drive")
elif(age1 <= 18):
    print("Dont drive")




    
# 1 nij theke banano input idea niye

age = int(input("Enter your age: "))

if (age >= 18):
    print("Can vote")
elif(age <= 18):
    print("Don't vote")



# 2 nije idea kore banano

name = input("enter your name:")

if(name == "faraby"):
    print("Welcome faraby")
    print("Your name faraby")
    print("Your age is 20")
    print("your city is Dhaka")
elif( name != "faraby"):
    print("Welcome stranger")
    print("Not varify User")
    
if(name == "Rofiq"):
    print("Welcome Rofiq")
    print("Your name Rofiq")
    print("Your age is 330")
    print("your city is Comilla")
elif( name != "Rofiq"):
    print("Welcome stranger")
    print("Not varify User")
                                                # tab deyake bola hoy indentation
    
# 3 
light = input("Enter the traffic light color: ")

if(light == "red"):
        print("Stop")
if(light == "yellow"):
        print("Ready")
if(light == "green"):
        print("Go")
elif (light == "pink"):
    print("light is broken")
    
# laster iff nij thke add kora
light = input("Enter the traffic light color: ")

if(light == "red"):
        print("Stop")
if(light == "yellow"):
        print("Ready")
if(light == "green"):
        print("Go")
if (light != "red" and light != "yellow" and light != "green" and light != "pink"):
        print("Invalid color")
elif (light == "pink"):
    print("light is broken")
    