from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/fazlur")
def fazlur():
    return "Hello, Fazlur!"
    
if __name__ == "__main__":
    app.run(debug=True)