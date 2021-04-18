# get the loan details
money_owed=float(input("how much do you owe in dollars\n"))
apr = float(input("What is the annual percentage rate?\n"))
payment= float(input("what wil be your monthly payment?\n"))
months = int(input("how many months will want to pay?\n"))

monthly_rate = apr/100/12
for i in range(months):
    interest_paid = money_owed * monthly_rate

    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("the last payment is ", money_owed,)
        print("you paid off the loan in", i+1, " months")
        break

    # make payment

    money_owed = money_owed - payment

    print("have paid", payment, "of which ", interest_paid, "was interest.", end=' ')
    print("now I owe", money_owed)