from flask import Flask, render_template, request, redirect, session   # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'secrets are no fun'

@app.route('/')          
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template("index.html") 

@app.route('/add_two', methods=['GET'])
def add_two():
    session['visits'] += 1
    return redirect('/')

@app.route('/destroy_session', methods=['GET'])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True) 