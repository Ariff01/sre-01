#1
a="Hi"
b="World"

print(a,b)

#2
a,b=0,10
while (a<=100):
  a=int(input("Key in a number more than 100: "))
while (b>=10):
  b=int(input("Key in a number less than 10: "))
print(int(a)/int(b))

#3
days=int(input("Key in the numbers of days: "))
hours=24*days
mins=60*hours
secs=60*mins
print(f"There are {hours} hours, {mins} mins and {secs} secs in {days} days")

#4
num=input("Key in a number: ")
if num=="1":
  print("Thank you")
elif num=="2":
  print("Well done")
elif num=="3":
  print("Correct")
else:
  print("Error Message")
  


  

