from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/new_page')
def new_page():
    return 'This is another page!'

#on Mac 
#FLASK_APP=hello.py flask run

#on Windows:
#export FLASK_APP=HELLO.PY (in different terminals you may use "set" instead of "export")
#flask run

##if __name__ =='__main__':
   # app.run(debug=True)

   # you can use this above code instead of running flask app(this is only good for one file and is trick with a package)
   #python hello.py
   #Debug mode makes updates when you tweek
