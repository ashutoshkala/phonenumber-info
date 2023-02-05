from flask import Flask
app1 = Flask(__name__) 
@app1.route("/")
def index():
    return "<h1>this is public page</h1>"
if __name__=='__main__':
    app1.run(host="0.0.0.0",port=5001,debug=True)
