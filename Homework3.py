Number = int(input("請輸入一個數值判斷是否為質數:"))
isPrimeNumber = True
for i in range(2, Number):
    if Number % i == 0:
        isPrimeNumber = False
        break
print(Number, "是質數") if isPrimeNumber else print(Number, "不是質數")