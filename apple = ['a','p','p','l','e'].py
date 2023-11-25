apple = ['a','p','p','l','e']
count = apple.count('p')
print("count of p :",count)

#helllooooo
a=1
b=2
print(a+b)

hihellohowareyou=('h','i','h','e','l','l','o','h','o','w','a','r','e','y','o','u')
count=hihellohowareyou.count('o')
print("count of o :",count)

def fib(n):
  a=0
  b=1
  for i in range (1,n+1):
    print(a)
    c=a+b
    a=b
    b=c
n=int(input("Enter the number:"))
fib(n)    

n=int(input("Enter the number:"))
sum=0
temp=n
while(n>0):
  r=n%10
  sum+=r**3
  n=n//10
if temp==sum:
  print("The number is a armstrong number")
else:
  print("The number is not a armstrong number")


  def fib(n):
    a=0
    b=1
    for i in range(1,n+1):
      print(a)
      c=a+b
      a=b
      b=c
    n=int(input("Enter the number:")) 
    fib(n) 

msg= hihellohowareyou
print(msg)
