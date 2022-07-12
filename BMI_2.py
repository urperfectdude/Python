
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2
bmi = round(bmi)
if bmi < 18.5 :
    print (f"your BMI is {bmi}, you are underweight")
elif bmi < 25 :
    print (f"your BMI is {bmi}, you have normal weight")
elif bmi < 30 :
    print (f"your BMI is {bmi}, you are slightly overweight")
elif bmi < 35 :
    print (f"your BMI is {bmi}, you are obese")
elif bmi > 35 :
    print (f"your BMI is {bmi}, you are clinically obese")
