from flask import Flask,render_template,request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/shell',methods=["GET","POST"])
def shell():
	if(request.method=='POST'):
		data = request.form['data']
		try:
			sh = subprocess.check_output(str(data),shell=True)
			print(dir(subprocess))
			return render_template('index.html',data=sh.decode(),classs="green")
		except Exception as error:
			return render_template('index.html',data=error,classs='red')
	else:
		return render_template('index.html')


if(__name__=="__main__"):
	app.run(debug=True)
print(dir(os))