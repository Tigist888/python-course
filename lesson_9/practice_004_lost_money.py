# This dictionary shows the bills each person has in their wallet and how many.
wallets = {
   'tom': {
       5: 2,  #Tom has two $5
       10: 1, # He also has one $10
   },
   'kelly': {
       1: 5
   },
   'joseph': {
       100: 1
   }
}

# Iterate over the wallets and check if each wallet has the 100.
# When you find the 100, print the name of the person that has it.

for person,wallet in wallets.items():
    if 100 in wallet:
        print(f"{person} has $100.")
        print(f"{person} has $100 and Quantity {wallet[100]}")
#or
for name,wallet in wallets.items():
    if 100 in wallet.keys():
        print(f"{name} has 100 dollar.")
        break
