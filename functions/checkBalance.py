import os

def checkBalance(user):
    file_name, balance = "0.txt", 0
    folder = os.listdir("./scripts")
    
    while file_name in folder:
        with open(f"./scripts/{file_name}", "r") as f:
            current_file = f.readlines()
            file_name = current_file[1].split(" ")[: -1]
            for transaction in current_file[2: ]:
                source, target, ammount = transaction.split(" ")
                source, target, ammount = source[: -1], target[: -1], float(ammount[: -1])

                if source == user:
                    balance -= ammount
                elif target == user:
                    balance += ammount
                    
    return balance