transaction=int(input("Number of Transaction?"))
budget=int(input("What's your budget?"))
ticket=0
travel=0
food=0
while transaction>0:
    
    type=int(input("Choose:- 1.Travel 2.Ticket 3.Food"))
    spent=int(input("How much you spent?"))
    budget-=spent
    if type==1:
        travel+=spent
    elif type==2:
        ticket+=spent
    else: food+= spent
    if budget<=0:
        print("Your budget exhausted!")
        break

