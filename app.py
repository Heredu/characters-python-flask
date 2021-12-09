from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


@app.route('/',)
def home():
    #if request.method=='POST':
        # Handle POST Request here
        return render_template('personajes/index.html')
   # return render_template('python-personajes-disney/index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)