from flask import Flask,render_template,abort
import os,json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html',titles=os.listdir('/home/shiyanlou/files')) #'hello world'

@app.route('/files/<filename>')
def file(filename):
	try:
		return render_template('file.html',content = read_file('/home/shiyanlou/files/'+ filename+'.json'))
	except:
		abort(404)

def read_file(filename):
	with open(filename,'r') as f:
		data = json.loads(''.join(f.readlines()))
	return data['title'],data['created_time'],data['content']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

app.run(port=3000)
