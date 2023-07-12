print("Loan Calculator")

first_money = int(input("Enter your loan amount > "))
loan = first_money
apr = 0.05
print("APR is 0.05 as defaoult.")
for i in range(10):
  loan+=(loan*apr)
  print("Year", i+1, "is", round(loan,2))

print("You paid ",round(loan-first_money,2), "TRY in insterest!")
