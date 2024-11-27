from flask import Flask, render_template, request
from functions.p2p import P2PNode

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/send")
# def send():
#     msg = request.args.get("name")
    
#     node.send_messages(msg)
    
#     return render_template("index.html")

@app.route("/ask_check_balance")
def ask_check_balance():
    return render_template("check_balance/ask.html")

@app.route("/check_balance", methods = ["POST"])
def check_balance():
    user = request.values["user"]
    balance = node.send_messages("check_balance", user)
    
    return render_template("check_balance/result.html", user = user, balance = balance)

@app.route("/ask_check_logs")
def ask_check_logs():
    return render_template("check_logs/ask.html")

@app.route("/check_logs", methods = ["POST"])
def check_logs():
    user = request.values["user"]
    logs = node.send_messages("check_logs", user)
    
    return render_template("check_logs/result.html", user = user, logs = logs)
    
@app.route("/ask_transaction")
def ask_transaction():
    return render_template("transaction/ask.html")
    
@app.route("/transaction", methods = ["POST"])
def transaction():
    user = request.values["user"]
    amount = request.values["amount"]
    result = node.send_messages("transaction", f"{user} {amount}")
    print(result)
    
    return render_template("transaction/result.html", result = result)

if __name__ == "__main__":
    ip, port = "140.123.97.108", 8001
    peers = [("140.123.104.113", 8001)]
    node = P2PNode()
    node.start()
    
    app.run()