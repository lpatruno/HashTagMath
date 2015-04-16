from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/model')
def model_test():
    return None
    
    
@app.route('/user/<name>')
def test_variables(name):
    return "String: %s" % name
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
