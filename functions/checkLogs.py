import os

def checkLogs(user):
    file_name, logs = "0.txt", []
    folder = os.listdir("./scripts")
    
    while file_name in folder:
        with open(f"./scripts/{file_name}", "r") as f:
            current_file = f.readlines()
            file_name = current_file[1].split(" ")[: -1]
            for transaction in current_file[2: ]:
                source, target, amount = transaction.split(", ")

                if source == user or target == user:
                    logs.append(transaction)
    
    return logs