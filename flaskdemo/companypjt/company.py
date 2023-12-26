from flask import Flask,render_template,request
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
        name = request.form['name']
        password = request.form['password']
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO company(name,password) VALUES (%s,%s)",(name,password))
        mysql.connection.commit()
    return render_template("comp.html")
@app.route('/view')
def view():
 cur= mysql.connection.cursor()
 cur.execute("SELECT * FROM company")
 res=cur.fetchall()   
 return render_template("view.html",datas=res)

@app.route('/update',methods=['POST'])
def update():
 id = request.form['id']
 name = request.form['name']
 password = request.form['password']
 cur= mysql.connection.cursor()
 cur.execute('UPDATE company SET name = %s, password= %s where id = %s',(id,name,password))
 res = mysql.connection.commit()
 return render_template ('view.html',datas=res)
 

if __name__=='__main__':
    app.run(debug=True)
    


