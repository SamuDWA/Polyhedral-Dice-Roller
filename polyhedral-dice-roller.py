import random

language = input("Choose between: English; Portuguese: ").lower()

if language == "english":
  stop = "no"
  while stop == "no":
    dice = input("Which dice do you want?: D4; D6; D8; D10; D12; D20; D010: ").upper()

    if dice == "D4":
        print("The number is:", random.randint(1, 4))
    elif dice == "D6":
        print("The number is:", random.randint(1, 6))
    elif dice == "D8":
        print("The number is:", random.randint(1, 8))
    elif dice == "D10":
        print("The number is:", random.randint(1, 10))
    elif dice == "D12":
        print("The number is:", random.randint(1, 12))
    elif dice == "D20":
        print("The number is:", random.randint(1, 20))
    elif dice == "D010":
        print("The number is:", random.randrange(0, 100, 10))
    else:
        print("Invalid dice selection!")

    stop = input("Do you want to stop? (yes or no): ").lower()
    if stop == "yes":
      print("Goodbye!")
      break

else:
  parar = "nao"
  while parar == "nao":
    dado = input("Qual dado você quer?: D4; D6; D8; D10; D12; D20; D010: ").upper()
    
    if dado == "D4":
        print("O número é:", random.randint(1, 4))
    elif dado == "D6":
        print("O número é:", random.randint(1, 6))
    elif dado == "D8":
        print("O número é:", random.randint(1, 8))
    elif dado == "D10":
        print("O número é:", random.randint(1, 10))
    elif dado == "D12":
        print("O número é:", random.randint(1, 12))
    elif dado == "D20":
        print("O número é:", random.randint(1, 20))
    elif dado == "D010":
        print("O número é:", random.randrange(0, 100, 10))
    else:
            print("Seleção de dado inválida!")

    parar = input("Você quer parar? (sim ou nao): ").lower()
    if parar == "sim":
      print("Até logo!")
      break
