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

@app.rote('/getMonthlyForCurriculum',methods = ['GET'])
def getMonthlyForCurriculum():
	board = request['board']
	cur = con.cursor()
	cur.execute("SELECT    from ")
	rows = cur.fetchall()
	return rows

@app.route('getClicksForCurriculum',methods=['GET'])
def getClicksForCurriculum():
	board=['board']
	cur=con.cursor()
	cur.execute("SELEC")

def getCityForCurriculum()

def getTechForCurriculum()

@app.route('/getDailyForCurriculum', methods = ["GET"])
def getDailyForCurriculum():
	board = request['board']
	cur = con.cursor()
	cur.execute("SELECT Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7 from school_level where Board = "+board)
	rows = cur.fetchall()
	return rows	

@app.rote('/getMonthlyForCurriculum',methods=['GET'])
def getMonthlyForCurriculum():
	board = request['board']
	cur = con.cursor()
	cur.execute("SELECT Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7 from school_level where Board = "+board)
	rows = cur.fetchall()
	return rows	

@app.route('/getClicksForCurriculum',methods=['GET'])
def getClicksForCurriculum():
	board = request['board']
	cur = con.cursor()
	cur.execute("SELECT click from school_level where Board = "+board)
	rows = cur.fetchall()
	return rows	

@app.route('/getCityForCurriculum')
def getCityForCurriculum():
	board = request['board']
	cur = con.cursor()
	cur.execute("SELECT city from school_level where Board = "+board)
	rows = cur.fetchall()
	return rows	


@app.route('/getTechForCurriculum',methods=["GET"])
def getTechForCurriculum():
	board = request['board']
	cur = con.cursor()
	cur.execute("SELECT tech from school_level where Board = "+board)
	rows = cur.fetchall()
	return rows	


@app.route('/getDailyForGrade',methods=["GET"])
def getDailyForGrade():
	curr = request['curriculum']
	grade = request['grade']
	cur=con.cursor()
	cur.execute("SELECT Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7 from school_level where Board = "+curr+"and grade="+grade)
	rows = cur.fetchall()
	return rows

@app.route('/getDailyForGradeAndWeek',methods=["GET"])
def getDailyForGradeAndWeek():
	curr = request['curriculum']
	grade = request['grade']
	week = request['week']
	cur=con.cursor()
	cur.execute("SELECT Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7 from school_level where Board = "+curr+"")
	rows = cur.fetchall()
	return rows

@app.route('/getDailyforWeek',methods=["GET"])
def getDailyforWeek():
	curr = request['curriculum']
	week = request['week']
	cur=con.cursor()
	cur.execute("SELECT Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7 from school_level where Board = "+curr+" and week ="+week)
	rows = cur.fetchall()
	return rows


app.run(debug=True)


