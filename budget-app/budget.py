

  
class Category:
 def __init__(self, name):
   self.name = name
   self.ledger = list()

 def __str__(self):
   title = f"{self.name:*^30}\n"
   items = ""
   total = 0
   for index in self.ledger:
       items += f"{index['description'][0:23]:23}" +f"{index['amount']:>7.2f}\n"
       total += index['amount']
   output = title + items + "Total: " + str(total)
   return output

 def deposit(self, amount, description = ""):
   self.ledger.append({"amount" : amount, "description" : description})

 def withdraw(self, amount, description = ""):
   if (self.check_funds(amount)):
     self.ledger.append({"amount" : -abs(amount), "description" : description})
     return True
   return False

 def get_balance(self):
   balance = 0
   for index in self.ledger:
     balance += index["amount"]

   return balance

 def transfer(self, amount, category):
   if (self.check_funds(amount)):
     self.withdraw(-abs(amount), "Transfer to " + category.name)
     category.deposit(amount, "Transfer from "+ self.name)
     return True
   return False

 def check_funds(self, amount):
   if (self.get_balance() >= amount):
     return True
   return False 
 def get_withdrawls(self):
     total = 0
     for item in self.ledger:
         if item["amount"] < 0:
             total += item["amount"]
     return total



def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    rounded = list(map(lambda x: (x/total), breakdown))
    return rounded
def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o" + (" "*2)
            else:
                cat_spaces += " "*3
        res+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i-= 10

    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        nameStr = " " * 5
        for name in names:
            if x >= len(name):
                nameStr += " " * 3
            else:
                nameStr += name[x] + " " * 2

        if(x != len(maxi) -1):
            nameStr += '\n'

        x_axis += nameStr

    res += dashes.rjust(len(dashes)+4) + '\n' + x_axis
    return res
