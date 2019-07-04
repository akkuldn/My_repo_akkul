"""
Calculator program
"""
class Calculator():
    def add(self,var1,var2):
        sum1=var1+var2
        print(sum1)
    def sub(self,var1,var2):
        diff=var1-var2
        print(diff)
    def mul(self,var1,var2):
        prod=var1*var2
        print(prod)  
    def div(self,var1,var2):
        divide=var1/var2
        print(divide)
if __name__=='__main__':
    calculator_obj=Calculator()
    val1=int(input("enter 1st value"))
    val2=int(input("enter 2nd value"))
    op=int(input("enter 1 for addition\n2 for subraction\n3 for multiplication\n4 for divison"))
    if(op==1):
        calculator_obj.add(val1,val2)
    if(op==2):
        calculator_obj.sub(val1,val2)
    if(op==3):
        calculator_obj.mul(val1,val2)
    if(op==4):
        calculator_obj.div(val1,val2)
