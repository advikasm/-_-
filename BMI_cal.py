#for Beginners: Create a command-line BMI calculator in Python. Prompt users for their weight 
#(in kilograms) and height (in meters). Calculate the BMI and classify it into categories 
#(e.g., underweight, normal, overweight) based on predefined ranges. Display the BMI result and 
#category to the user.

def take_info():
    print("****************Welcome to the BMI Calculator****************")
    name = input("Please enter your name here: ")
    weight = float(input("{}, enter your weight in kilograms (KG) :  ".format(name)))
    height = float(input("{}, enter your height in meters :  ".format(name)))
    check_bmi(height, weight, name)

def check_bmi(h,w,name):
    bmi = w/(h*h)
    if bmi<18.5:
        print("\nYou are under weight")
    elif 18.5< bmi <=24.9:
        print("\nYou have normal weight")
    elif 25<=bmi<=29.9:
        print("\nOverweight")
    else:
        print("\nYou are obese")

    print("\n{}, your BMI is {}".format(name, bmi))

def healthy_measures():
    print("\n*****Healthy Measures*****.\n ~Learn more about overweight and obesity.\n ~Increase Physical Activity.\n ~Moving more can lower your risk factors for heart disease.\n ~Eat a Heart-Healthy Diet Eating a healthy diet is the key to heart disease prevention.")

take_info()
healthy_measures()