from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", items=["Apple", "Banana", "Cherry"], recTitle = "Home page")

@app.route("/apple")
def apple():
    return render_template("apple.html", recTitle = "apple" , )

@app.route("/banana")
def banana():
    return render_template("banana.html", recTitle = "banana", )

@app.route("/cherry")
def cherry():
    return render_template("cherry.html", recTitle = "cherry", )



if __name__ == "__main__":
    app.run(debug=True)