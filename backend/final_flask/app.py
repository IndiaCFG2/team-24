from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import sqlite3
from flask import g
from flask import request
from flask import jsonify
from flask import redirect, url_for
import json

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

@app.route('/admin/form1')
def form1():
	return render_template('form1.html')

@app.route('/admin/form2')
def form2():
	return render_template('form2.html')

@app.route('/admin/grade_wise')
def grade_wise():
	return render_template("grade_wise.html")

@app.route("/admin/tables")
def tables():
	return render_template("tables.html")

@app.route('/week')
def week():
	return render_template('week.html')

@app.route('/day')
def day():
	return render_template('day.html')

@app.route('/generateURL', methods = ["GET", "POST"])
def generateURL():
	data = json.loads(request.data)
	print(request.data)
	sid = data['id']
	tech = data['tech']
	subj = data['subj']
	gr = data['gr']
	wk = data['wk']
	day = data['day']
	final_id = sid+tech.upper()[0]+"G"+str(int(gr))+"S"+subj+"W"+str(int(wk))+"D"+str(int(day))
	url = '127.0.0.1:5000/getURL?id='+final_id;
	return jsonify({'data': url})

@app.route('/getURL', methods = ["GET", "POST"])
def getURL():
	fid = request.args.get('id')
	sid = fid[:4]
	tech = "Low" if fid[4] == 'L' else 'High'
	grade = int(fid[6])
	subj = 'Maths' if fid[8] == 'M' else ('EVS' if fid[10] == 'S' else 'English')
	week = int(fid[10])
	day = int(fid[-1])
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("SELECT Link from lessonData where \"School ID\" = ? AND Tech = ? and Grade = ? and Subject = ?  and Week = ? and Day = ?", [sid, tech, grade, subj, week, day]);
	rows = cur.fetchall()
	cur.execute("UPDATE lessonData SET Clicks = Clicks + 1 WHERE \"School ID\" = ? AND Tech = ? and Grade = ? and Subject = ?  and Week = ? and Day = ?", [sid, tech, grade, subj, week, day]);
	con.commit();
	print(rows)
	return redirect(rows[0][0], code = 302)

@app.route('/schoolData', methods = ["GET", "POST"])
def schoolData():
	name = request.form['ename'];
	sid = request.form['uname'];
	curr = request.form['curr'];
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("INSERT INTO schoolData VALUES(?, ?, ?)", [name, sid, curr]);
	con.commit()
	return redirect(url_for('form1'))

@app.route('/getCurr', methods=["GET", "POST"])
def getCurr():
	data = json.loads(request.data)
	sid = data['sid']
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("SELECT Curriculum FROM schoolData WHERE \"School ID\" = ?", [sid])
	rows = cur.fetchall()
	print(rows)
	return jsonify({'data': rows})

@app.route('/lessonData', methods = ["GET", "POST"])
def lessonData():
	sid = request.form['sid']
	tech = request.form['tech']
	grade = request.form['grade']
	subj =	request.form['subject']
	week = request.form['week']
	day = request.form['day']
	link = request.form['url']
	clicks = 0
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("INSERT INTO lessonData VALUES(?, ?, ?, ?, ?, ?, ?, ?)", [sid, tech, grade, subj, week, day, link, clicks]);
	con.commit()
	return redirect(url_for('form2'))

@app.route('/getDailyForCurriculum', methods = ["GET", "POST"])
def getDailyForCurriculum():
	data = json.loads(request.data)
	board = data['board']
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("SELECT SUM(Day_1), SUM(Day_2), SUM(Day_3), SUM(Day_4), SUM(Day_5), SUM(Day_6), SUM(Day_7) from school_level where Board = ? ",[board])
	rows = cur.fetchall()
	return jsonify({'data': rows})

@app.route('/getMonthlyForCurriculum', methods = ["GET", "POST"])
def getMonthlyForCurriculum():
	data = json.loads(request.data)
	board = data['board']
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("SELECT SUM(Jan), SUM(Feb), SUM(Mar), SUM(Apr), SUM(May), SUM(Jun), SUM(Jul), SUM(Aug), SUM(Sep), SUM(Oct), SUM(Nov), SUM(Dec) from school_level where Board = ? ",[board])
	rows = cur.fetchall()
	t = ()
	for i in rows[0]:
		t = t + (i//1000,)
	return jsonify({'data': [t]})

@app.route('/getGradeForCurriculum', methods = ["GET", "POST"])
def getGradeForCurriculum():
	data = json.loads(request.data)
	board = data['board']
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	t = ()
	for i in range(5):
		cur.execute("SELECT SUM(Day_7) from gen_level where Board = ? AND Grade = ?",[board, "G"+str(i+1)])
		rows = cur.fetchall()
		t = t + (rows[0][0]//100,)
	return jsonify({'data': [t]})

@app.route('/getNumberOfActive', methods = ["GET", "POST"])
def getNumberOfActive():
	data = json.loads(request.data)
	board = data['board']
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("SELECT COUNT(*) from school_level where Board = ? ",[board])
	rows = cur.fetchall()
	return jsonify({'data': rows})

@app.route('/getNamesOfSchools', methods = ["GET", "POST"])
def getNamesOfSchools():
	data = json.loads(request.data)
	board = data['board']
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("Select \"School Name\" from school_level where Board = ?",[board])
	rows = cur.fetchall()
	return jsonify({'data': rows})

@app.route('/getTechForCurriculum', methods = ["GET", "POST"])
def getTechForCurriculum():
	data = json.loads(request.data)
	board = data['board']
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("SELECT SUM(Day_1), SUM(Day_2), SUM(Day_3), SUM(Day_4), SUM(Day_5), SUM(Day_6), SUM(Day_7) from gen_level where Board = ? AND Tech = ?",[board, "Low Tech"])
	rows = cur.fetchall()
	t = ()
	for i in rows[0]:
		t = t + (i//100,)
	send = { 'low': [t] }
	cur.execute("SELECT SUM(Day_1), SUM(Day_2), SUM(Day_3), SUM(Day_4), SUM(Day_5), SUM(Day_6), SUM(Day_7) from gen_level where Board = ? AND Tech = ?",[board, "High Tech"])
	rows = cur.fetchall()
	t = ()
	for i in rows[0]:
		t = t + (i//100,)
	send['high'] = [t]
	return jsonify({'data': send})


@app.route('/getCityForCurriculum', methods = ["GET", "POST"])
def getCityForCurriculum():
	data = json.loads(request.data)
	board = data['board']
	con = sqlite3.connect("chart1.db")  
	cur = con.cursor()
	cur.execute("SELECT City, COUNT(*) from school_level where Board = ? group by City ",[board])
	rows = cur.fetchall()
	print("HELLO", rows)
	res, labels = [], []
	for i in rows:
		if i[1] >= 4:
			res.append(i[1])
			labels.append(i[0])
	send = {'res': res, 'labels': labels}
	return jsonify({'data': send})


app.run(debug=True)


