from flask import Flask
app = Flask(__name__)

# Requisição: http://localhost:5000/
# Resposta: Tô de pé!

@app.route("/")
def teste():
    return "Tô de pé!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
