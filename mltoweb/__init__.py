import os
import pickle
__version__ = (0, 0, 1)

bottle_code = r'''
from bottle import run, get, post, request
import pickle

with open('estimator.pickle', 'rb') as fl:
    est = pickle.load(fl)
@get('/')
def main():
    html = """<html>
    <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    </head>
    <body>
    <div class='container'>
    <a href="/reload-classifier"><button class='btn'>Reload classifier from file</button></a><hr>
        <table class='table'>
        <form action='/form-receptor' method='post'>
            <tbody>
            {inputs}
            <tr><td><input type='submit' value='Submit'></input></td></tr>
            </tbody>
        </form>
        </table>
    </div>
    </body>
    </html>"""
    return html

@post('/form-receptor')
def mainform():
    names = {names}
    values = [float(request.POST[i]) for i in names]
    prediction = est.predict([values])
    html = '<p>Prediction is: ' + str(prediction)
    html += '</p><br> <a href="/">Another prediction</a>'
    return html

@get('/reload-classifier')
def reload_classifier():
    global est
    with open('estimator.pickle', 'rb') as fl:
        est = pickle.load(fl)
    return 'Done<br><a href="/">Make a prediction</a>'
run(host='localhost', port=8080, debug=True)
'''

def make_web(est, X, y, path):
    if not os.path.exists(path):
        os.mkdir(path)
    est_path = os.path.join(path, 'estimator.pickle')
    est.fit(X, y)
    with open(est_path, 'wb') as fl:
        pickle.dump(est, fl)

    inputs = ['<tr><td><label>{col}</label></td><td><input type="text" name="{col}"></input></td></tr>'.format(col=col) for col in X.columns]
    inputs = '\n'.join(inputs)
    code = bottle_code.format(inputs=inputs, names=list(X.columns))
    with open(os.path.join(path, 'website.py'), 'w') as fl:
        fl.write(code)
