from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

#def settask():
    #return render_template("")
if __name__ == "__main__":
    app.run(debug=True)
