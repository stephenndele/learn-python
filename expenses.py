# expenses = [10.50, 10, 56, 5, 6, 7, 8]

total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("Enter Expense: ")))

total = sum(expenses)

# for x in expenses:
#     sum = sum + x

print("You spent", total, "for breakfast this week")