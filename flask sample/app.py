from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL


app=Flask(__name__)
mysql = MySQL(app)

app.secret_key = 'your secret key'
 
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sahana#26812681'
app.config['MYSQL_DB'] = 'company'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=="POST":
        name = request.form['username']
        password = request.form['password']
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO company(name,password) VALUES (%s,%s)",(name,password))
        mysql.connection.commit()
    return render_template("index.html")



@app.route('/view')
def view():
 cur= mysql.connection.cursor()
 cur.execute("SELECT * FROM company")
 res=cur.fetchall()   
 return render_template("view.html",datas=res)




@app.route('/update/<string:id>',methods=['GET', 'POST'])
def update(id):
    cur= mysql.connection.cursor()
    cur.execute("select * from company where id=%s", [id])
    res=cur.fetchone()
    if request.method=="POST":
        name = request.form['username']
        password = request.form['password']
        sql="UPDATE company SET name=%s,password=%s where id=%s"
        user = (name,password,id)
        cur.execute(sql, user)
        mysql.connection.commit()
        return redirect(url_for("view"))
    return render_template("update.html", man=res)


@app.route('/delete/<string:id>',methods=['GET', 'POST'])
def delete(id):
    cur= mysql.connection.cursor()
    cur.execute("delete from company where id=%s", [id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("home"))

if __name__=='__main__':
    app.run(debug=True)


