from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os,json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'

db = SQLAlchemy(app)

class File(db.Model):
	__tablename__ = 'file'
	id = db.Column(db.Integer,primary_key = True, autoincrement= True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
	category = db.relationship('Category',backref = 'categorys')
	content = db.Column(db.String(128))
	def __init__(self,title,created_time,category,content):
		self.title = title
		self.created_time = created_time
		self.category = category
		self.content = content
	def __repr__(self):
		return '<File(title={})>'.format(self.title)

class Category(db.Model):
	__tablename__ = 'category'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	name = db.Column(db.String(50))
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return '<Category(name={})>'.format(self.name)

@app.route('/')
def index():
	file_list = db.session.query(File).all()
	dict1 = {}
	for each in file_list:
		dict1[each.id] = each.title
	return render_template('index.html',dict = dict1)

@app.route('/file/<file_id>')
def file(file_id):
	try:
		file = db.session.query(File).filter('id='+str(file_id)).first()
		return render_template('file1.html',title = file.title,content = file.content,created_time = file.created_time,category = file.category.name)
	except:
		abort(404)

if __name__ == '__main__':
	app.run(port=3000)