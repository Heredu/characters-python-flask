from flask import Flask,redirect,url_for,render_template,request
from flaskext.mysql import MySQL

app=Flask(__name__)


mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='bhekfp2adliaxycgkxgz-mysql.services.clever-cloud.com'
app.config['MYSQL_DATABASE_USER']='uiruianxd7algkb6'
app.config['MYSQL_DATABASE_PASSWORD']='IcStdDY4LsVAA1lQex1h'
app.config['MYSQL_DATABASE_DB']='bhekfp2adliaxycgkxgz'
mysql.init_app(app)

@app.route('/',)
def home():

    sql="SELECT * FROM `personajes`;"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    
    personajes=cursor.fetchall()
    print(personajes)

    conn.commit()
    #if request.method=='POST':
    # Handle POST Request here
    return render_template('personajes/index.html', personajes=personajes)
   # return render_template('python-personajes-disney/index.html')

@app.route('/create')
def create():
    return render_template('personajes/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _name=request.form['txtName']
    _history=request.form['txtHistory']
    _photo=request.form['txtPhoto']
    
    sql="INSERT INTO `personajes` (`id`, `imagen`, `nombre`, `edad`, `peso`, `historia`, `asociaciones`, `createdAt`, `updatedAt`) VALUES (NULL, %s, %s, '1', '1', %s, 'OTROS', '2021-12-09 00:00:00', '2021-12-09 00:00:00');"
    
    date=(_photo, _name, _history)
    
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,date)
    conn.commit()
    #if request.method=='POST':
    # Handle POST Request here
    return render_template('personajes/index.html')
   # return render_template('python-personajes-disney/index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)