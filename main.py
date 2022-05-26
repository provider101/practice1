from distutils.log import debug
from flask import Flask
app=Flask(__name__)

@app.route('/')
def prac1():
    return 'first program'
@app.route('/')
def prac2():
    return 'second'

if __name__=="__main__":
    app.run(debug=True)