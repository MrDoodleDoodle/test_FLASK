from flask import Flask, request, render_template, url_for, request, redirect
from data import Data
import time, pickle
import os
import glob


app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('start_page'))
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    error = None
    if request.method == 'POST':
        pw = request.form["password"]
        if pw == "1":
            return redirect(url_for('start_page'))
        else:
            error = "wrong password"
    return render_template('login_page.html', error = error)

@app.route('/search')
def start_page():
    Data().combine2(pickle.load(open('Data.dat', 'rb')), "lolololololo", 2, 'start_page')
    #Data().combine("all_file_structure.txt", 'lolololololo')
    return render_template('start_page.html', depth = "2")

@app.route('/search', methods=['POST'])
def search_page():
    if request.method == 'POST':
        print(request.form)
        try:
            text = request.form['text']
        except:
            text = ''
        depth = int(request.form['depth'])
        if depth ==0:
            depth = 20

    else:
        text = ""
    start_time = time.time()
    print(depth)
    name = text+str(depth)
    files = glob.glob('templates/*')
    for f in files:
        if f != "templates\\base.html" and f != "tamplates/base.html":
            print(f)
            os.remove(f)
    Data().combine2(pickle.load(open('Data.dat', 'rb')), text, depth, name)
    #Data().combine("all_file_structure.txt", text)
    print(time.time()-start_time)

    if depth ==20:
        depth = 0
    print(depth)
    return render_template(f'{name}.html', depth = depth)




if __name__ == "__main__":
	#app.run(host = '0.0.0.0', port = 5000, debug=True)
    app.run(debug=True)
