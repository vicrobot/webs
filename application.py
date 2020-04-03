from flask import Flask, request, render_template, url_for
import matplotlib.pyplot as plt
import numpy as np
import os

#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


#engine=  create_engine(os.getenv("DATABASE_URL") )
#db = scoped_session(sessionmaker(bind = engine) )

@app.route("/")
def index():
    return render_template("index.html", list_1 = enumerate(['sin(x)','cos(x)', 'tan(x)']))
    
@app.route("/plot", methods= ['POST'])
def plot():
    xs = request.form.get("inp1")
    ys = request.form.get("inp2")
    try:
        if ',' in xs:
            xl = [int(i.strip()) for i in xs.split(',') if i]
            yl = [int(i.strip()) for i in ys.split(',') if i]
        else:
            xl = [int(i.strip()) for i in xs.split(' ') if i]
            yl = [int(i.strip()) for i in ys.split(' ') if i]
        if len(xl) != len(yl): raise ValueError
    except:
        return render_template("error.html", message="wrong input")
    plt.style.use('dark_background')
    plt.plot(xl, yl)
    plt.title("Line Plot")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid('True')
    for x, y in zip(xl, yl):
        plt.text(x,y, f"({x},{y})" )
    imgname  = 'static/image.jpg'
    plt.savefig(imgname)
    #return render_template("plot.html",  img_url = url_for('static', filename='image.jpg')) #this too is correct
    return render_template("plot.html",  img_url = imgname)

if __name__ == "__main__":
    app.run(debug=True)
