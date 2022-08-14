class simplecalc():
    def add(self):
        num=num1+num2
        return num
    def sub(self):
        num=num1-num2
        return num
    def mul(self):
        num=num1*num2
        return num    
    def div(self):
        num=num1/num2
        return num    
ans=simplecalc()
retry=''
while retry!="exit":    
    num1=int(input("Please key in 1st number: "))
    num2=int(input("Please key in 2nd number: "))      
    operator=input("Please input an operator to do the arithmetic operation (+,-,*,/): ")

    if operator=='+':
          print(ans.add())
    elif operator=='-':
          print(ans.sub())
    elif operator=='*':
          print(ans.mul())            
    elif operator=='/':
          print(ans.div())    
    else:
          print("Operator not recognised, please try again")
    retry=input("Would you like to continue? (yes,exit): ").lower()

print("Thank you")
