distance_A=int(input("Enter the distance of Casa Manco: "))
distance_B=int(input("Enter the distance of Colosseum: "))
distance_C=int(input("Enter the distance of Vatican City: "))


if distance_A<distance_B and distance_A<distance_C:
    print("Go to Casa Manco")
elif distance_B<distance_A and distance_B<distance_C:
    print("Go to Colosseum")
else : print("Go to Vatican City")