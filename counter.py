from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key=('P.O.S')
# our index route will handle rendering our form
@app.route('/')
def index():
    try:
        session['num']
    except:
        session['num']=1
    else:
        session['num']+=1
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/double',methods=['GET','POST'])
def double():
    #session['num']+=1
    #print request.form['buttonAction']
    if request.form['buttonAction']=='double':
        session['num']+=1
    elif request.form['buttonAction']=='reset':
        session['num']=0
    return redirect('/')
app.run(debug=True)
