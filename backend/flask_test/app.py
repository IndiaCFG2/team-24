from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import sqlite3
from flask import g
  
con = sqlite3.connect("chart1.db")  

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/admin')
def admin():
	return render_template("admin.html")

@app.route('/admin/dashboard')
def dashboard():
	return render_template("dashboard.html")

@app.route('/admin/grade_wise')
def grade_wise():
	return render_template("grade_wise.html")

@app.route("/admin/tables")
def tables():
	return render_template("tables.html")

@app.route('/getDailyForCurriculum', methods = ["GET"])
def getDailyForCurriculum():
	board = request['board']
	cur = con.cursor()
	cur.execute("SELECT Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7 from school_level where Board = "+board)
	rows = cur.fetchall()
	return rows	

@app.route('/getMonthlyForCurriculum',methods=["GET"])
def getMonthlyForCurriculum():
	board=request['board']
	cur=con.cursor()
	cur.execute("SELECT ")
	rows=cur.fetchall()
	return rows

@app.route('/getClicksForCurriculum',methods=["GET"])
def getClicksForCurriculum():
	board=request['board']
	cur=con.cursor()
	cur.execute("SELECT ")
	rows=cur.fetchall()
	return rows


def getCityForCurriculum()

def getTechForCurriculum()

@app.route('/getDailyForCurriculum', methods = ["GET"])
def getDailyForCurriculum():
	board = request['board']
	cur = con.cursor()
	cur.execute("SELECT Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7 from school_level where Board = "+board)
	rows = cur.fetchall()
	return rows	

@app.rote('.')
def getMonthlyForCurriculum():

@app.route()...
def getClicksForCurriculum():

def getCityForCurriculum()

def getTechForCurriculum()


def getDailyForGrade():
	curr = request['curriculum']
	grade = request['grade']


def getDailyForGradeAndWeek():
	curr
	grade
	week

def getDailyforWeek():
	curr
	week



app.run(debug=True)


