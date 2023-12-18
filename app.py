from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def sam():
    return "This is my first Azure Page"
@app.route('/sec')
def puja():
    return "hello,how are you"
@app.route('/third')
def  rama():
    return render_template('index.html')
app.run(use_reloader=True,debug=True)







