n=1
Sum=0
Number = int(input("請輸入一個數值判斷是否為質數:"))
while True:
  if Number%n==0:
    Sum+=1
    if n==Number and Sum==2:
      print(Number,"是質數")
      break
  n+=1
  if n==Number and Sum>=2:
    print(Number,"不是質數")
    break