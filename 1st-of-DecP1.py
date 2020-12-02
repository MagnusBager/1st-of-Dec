expense_report = []

a,b = 0,0

while True:
  user_input = input("enter puzzle input")
  if user_input != "break":
    expense_report.append(int(user_input))
    continue
  break

for i in expense_report:
  for x in expense_report:
    if i + x == 2020 and i != x:
      a = i
      b = x

print(a*b)
