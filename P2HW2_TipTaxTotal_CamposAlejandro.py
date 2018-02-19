#CTI 110
#Feb.19 2018
#P2HW2 Tip, Tax, and Total
#Alejandro Campos

#foodCost, tipAmount, salesTax, totalCost

#Enter Food Cost.
foodCost=float(input ("Enter the cost of food:$ "))

# Calculate tip amount.
tipAmount =foodCost * 0.18

# Calculate tax amount.
salesTax =foodCost * 0.07

foodCost = foodCost+tipAmount+salesTax

#Total of Food cost + 18% tip + Sales tax 7%.

print ("Tip $", format (tipAmount, ".2f"))
print ("Tax $", format (salesTax, ".2f"))
print ("Total $", format (foodCost, ".2f"))
