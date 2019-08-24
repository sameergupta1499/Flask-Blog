from flask import Flask,render_template,url_for
from Form import RegistrationForm, LoginForm,Hi

app = Flask(__name__)
obj=Hi()
obj.hiEveryone()
posts= [
    {
        'author':'Author1',
        'title':'Post1',
        'content':'This is the content of the first Post',
        'date_posted':'16 Aug 2019',
    },
    {
        'author':'Author2',
        'title':'Post2',
        'content':'This is the content of the Second Post',
        'date_posted':'17 Aug 2019',
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template("home.html",posts=posts)

@app.route('/about')
def about():
    return render_template("about.html",title="About")

if __name__=="__main__":
    app.run(debug=True)
