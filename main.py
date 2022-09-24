# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from operator import ge

from flask import Flask, render_template, redirect, request, session
from flask_mysqldb import MySQL
from flask_session import Session
from django import apps
import datetime
import os
import shutil
from datetime import datetime, timedelta


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')


TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app = Flask(__name__, static_url_path='/static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ReadReview'
Session(app)
mysql = MySQL(app)

@app.route('/')
def homepage():
    try:
        return render_template("index.html")
    except Exception as e:
        return str(e)

@app.route('/about')
def aboutpage():
    return render_template("about.html")

@app.route('/contact')
def contactpage():
    return render_template("contact.html")

@app.route('/adminlogin')
def adminlogin():
    return render_template("adminlogin.html")

@app.route('/newuser')
def newuser():
    return render_template("newuser.html")

@app.route('/newbook')
def newbook():
    return render_template("newbook.html")

@app.route('/adminviewbooks')
def adminviewbook():
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' select * from newbook ''')
    datarows = cursor.fetchall()
    return render_template("adminviewbooks.html", rows=datarows)

@app.route('/userviewbooks')
def userviewbook():
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' select * from newbook ''')
    datarows = cursor.fetchall()
    return render_template("userviewbooks.html", rows=datarows)

@app.route('/userapplyreview')
def userapplyreview():
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' select * from newbook ''')
    datarows = cursor.fetchall()
    return render_template("userapplyreview.html", rows=datarows, msg="")


@app.route('/adminbookdelete')
def adminbookdelete():
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' select * from newbook ''')
    datarows = cursor.fetchall()
    return render_template("adminbookdelete.html", rows=datarows)

@app.route('/adminviewusers')
def adminviewusers():
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' SELECT   UserId, FirstName,  LastName,  EmailId,  PhoneNumber FROM newuser ''')
    datarows = cursor.fetchall()
    return render_template("adminviewusers.html", rows=datarows)

@app.route('/adminviewreviews')
def adminviewreviews():
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' select * from NewReview ''')
    datarows = cursor.fetchall()
    cursor.execute(
        '''SELECT Rating, COUNT(Rating) AS RatingCount FROM 
        newreview GROUP BY  Rating ''')
    countrows = cursor.fetchall()
    return render_template("adminviewreviews.html", rows=datarows, countrows=countrows)

@app.route('/userapplyreview1',  methods=['GET'])
def userapplyreview1():
    print("Apply Review Function")
    args = request.args
    id =  args.get("id")

    cursor = mysql.connection.cursor()
    sql = "select * from newbook where bookid = "+id
    print(sql)
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    datarows = cursor.fetchall()

    userid = session["userid"]
    cursor = mysql.connection.cursor()
    sql = "select * from newuser where userid = " + str(userid)
    print(sql)
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    userdata = cursor.fetchall()
    print(datarows[0])
    print(userdata[0])
    print(userdata[0][0])
    return render_template("userapplyreview1.html", msg="User Apply Review Page",
                       rows=datarows[0], userdata=userdata[0])

@app.route('/userapplyreview2', methods=['POST'])
def userapplyreview2():
    print("User Apply Review Function")
    if request.method == 'POST':
        bookid = request.form['bookid']
        bname = request.form['bname']
        aname = request.form['aname']
        pname = request.form['publisher']
        year = request.form['year']
        userid = request.form['userid']
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['emailid']
        phnum = request.form['phnum']
        rating = request.form['rating']
        comments = request.form['comments']

        cursor = mysql.connection.cursor()
        cursor.execute(
        ''' INSERT INTO NewReview(BookId, BookName, 
            AuthorName, PublisherName, PublishedYear, UserId, FirstName, LastName, EmailId, PhoneNumber, Rating, Comments)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ''',
            (bookid, bname, aname, pname, year, userid, fname, lname, email, phnum, rating, comments))
        mysql.connection.commit()
        cursor.close()
        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' select * from newbook ''')
        datarows = cursor.fetchall()
        return render_template("userapplyreview.html", rows=datarows, msg="Review Updated Successfully")


@app.route('/addbook', methods=['POST'])
def addBook():
    print("Add Book Function")
    if request.method == 'POST':
        bname = request.form['bname']
        aname = request.form['aname']
        pname = request.form['publisher']
        year = request.form['year']
        fname = request.form['fname']
        src_path = "C:\\Users\\Harshitha GR\\Desktop\\Images\\"+fname
        dst_path = "C:\\Users\\Harshitha GR\\Downloads\\OnlineReadReviewProject\\static\img\\"+fname
        shutil.copy(src_path, dst_path)

        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' INSERT INTO NewBook(BookName, 
            AuthorName, PublisherName, PublishedYear, Image)
            VALUES(%s, %s, %s, %s, %s) ''',
            (bname, aname, pname, year, fname))
        mysql.connection.commit()
        cursor.close()
    return render_template("newbook.html", msg="Book Added Success")


@app.route('/adduser', methods=['POST'])
def addUser():
    print("Add User Function")
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        uname = request.form['uname']
        pwd = request.form['pwd']
        email = request.form['emailid']
        phnum = request.form['phnum']

        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' INSERT INTO NewUser(FirstName, LastName, UserName, Password, EmailId, PhoneNumber) VALUES(%s, %s, %s, %s, %s, %s) ''',
            (fname, lname, uname, pwd, email, phnum))
        mysql.connection.commit()
        cursor.close()
    return render_template("newuser.html", msg="User Added Success")

@app.route('/admindeletebookpage1',  methods=['GET'])
def admindeletebookpage1():
    print("Delete Book Function")
    args = request.args
    id = args.get("id")

    cursor = mysql.connection.cursor()
    sql = "delete from newbook where bookid = ",id
    print(sql)
    cursor.execute(''' delete from newbook where bookid = %s ''',(id))
    mysql.connection.commit()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' select * from newbook ''')
    datarows = cursor.fetchall()

    return render_template("adminbookdelete.html", msg="Book Deleted Success", rows=datarows)

@app.route('/adminlogincheck', methods=['POST'])
def adminlogincheck():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pwd']
    print("Uname : ", uname, " Pwd : ", pwd);
    if uname == "admin" and pwd == "admin":
        return render_template("adminmainpage.html")
    else:
        return render_template("adminlogin.html", msg="UserName/Password is Invalid")

@app.route('/userlogincheck', methods=['POST'])
def userlogincheck():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pwd']
    print("Uname : ", uname, " Pwd : ", pwd)
    cursor = mysql.connection.cursor()
    cursor.execute(
        ''' Select * from NewUser where UserName = %s and Password =%s ''', (uname, pwd))
    row = cursor.fetchone()
    if row:
        session["userid"] = row[0]
        session["username"] = row[1] + row[2]
        return render_template('usermainpage.html')
    else:
        return render_template("userlogin.html", msg="UserName/Password is Invalid")


@app.route('/userlogin')
def userlogin():
    return render_template("userlogin.html")


@app.route('/usermainpage')
def usermainpage():
    return render_template("usermainpage.html")


@app.route('/adminmainpage')
def adminmainpage():
    return render_template("adminmainpage.html")


if __name__ == "__main__":
    app.run(debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
