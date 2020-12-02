expense_report = []
x,y,z = 0,0,0

while True:
  user_input = input("enter puzzle input")
  if user_input != "break":
    expense_report.append(int(user_input))
    continue
  break

for a in expense_report:
  for b in expense_report:
    for c in expense_report:
      if a + b + c == 2020 and a != 0 and b != 0 and c != 0:
        x = a
        y = b
        z = c

print(x*y*z)
