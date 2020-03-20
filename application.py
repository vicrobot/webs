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
    return render_template("index.html")

@app.route("/plot", methods= ['POST'])
def plot():
    x = int(request.form.get("inp1"))
    y = int(request.form.get("inp2"))
    plt.style.use('dark_background')
    plt.scatter([x], [y])
    plt.title("Scatter Plot")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid('True')
    plt.text(x,y, f"({x},{y})" )
    imgname  = 'static/image.jpg'
    plt.savefig(imgname)
    #return render_template("plot.html",  img_url = url_for('static', filename='image.jpg')) #this too is correct
    return render_template("plot.html",  img_url = imgname)

if __name__ == "__main__":
    app.run(debug=True)
