"""
Sample program
"""
def get_input():
    height=float(input("Enter height of student in meter"))
    weight=int(input("enter weight of student in kg"))
    return height,weight

def calculate_BMI(height,weight):
    bmi= weight/(height*height)
    print("the BMI is",bmi)
    if(bmi<=18.5):
        print("underweight")
    elif(bmi>18.5 and bmi<=24.9):
        print("You are normal")
    elif(bmi>=25 and bmi<29.9):
        print("overweight")
    else:
        print("obese")

if __name__=='__main__':
   height,weight= get_input()
   calculate_BMI(height,weight)
