num = int(input("Input the number: "))
sum = 0
rem = 0

while num != 0:
      rem = num % 10
      sum = sum + rem
      num = num // 10
      
print(sum)