Ask the user for a number.
Output a count starting with 0.
Display the count number if it is not divisible by 3 or 5.
Replace every multiple of 3 with the word "fizz."
Replace every multiple of 5 with the word "buzz."
Replace multiples of both 3 and 5 with "fizz buzz."
Continue counting until the number of integers replaced with "fizz," "buzz," or "fizz buzz" reaches the input number.
The last output line should read "TRADITION!!"

#code
num=int(input("Please key in a number: "))
c=0;d=0
while (c!=num):
              if d==0:
                print(d)
              elif d%3==0 and d%5==0:
                print('fizz buzz')
                c+=1
              elif d%3==0:
                print('fizz')
                c+=1
              elif d%5==0:
                print('buzz')
                c+=1 
              else:
                print(d)
              d+=1
print('TRADITION!!')  
