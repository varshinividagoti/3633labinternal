from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('reg.html')
@app.route('/submit',methods=['POST'])
def submit():
    lname=request.form["lname"]
    fname=request.form["fname"]
    age=request.form["age"]
    return render_template('success.html',lname=lname,fname=fname,age=age)
if __name__=='__main__':
    app.run( host="0.0.0.0",port=5000,debug=True)