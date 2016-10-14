from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def idx():
	return render_template('index.html')

@app.route('/result',methods=['POST'])
def submit():
    data = request.form
    print data
    return render_template('result.html', data=data)
app.run(debug=True)	