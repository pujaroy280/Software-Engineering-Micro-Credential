from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Connect to database
app.config ['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:SWEmicro123!@localhost/demoDB'
db = SQLAlchemy(app)

# Define db model
class Data(db.Model):
    __tablename__ = "data"
    id=db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique = True)
    username = db.Column(db.String(120))

    def __init__(self,email, username):
        self.email = email
        self.username = username

@app.route("/") 
def hello():
    return render_template("checkout.html")

# Get information from your form in checkout.html, when the submit button is clicked
@app.route('/', methods=['POST'])
def thankyou():
    if request.method == "POST":
        email = request.form["emailAddress"]
        username = request.form["username"]
        print(request.form)
    # Last step: commit
    data = Data(email,username)
    db.session.add(data)
    db.session.commit() #execute
    return render_template('thankyou.html')



if __name__ == '__main__':
    app.debug=True
    app.run()


