from flask import Flask, render_template, jsonify
import pandas as pd
import random

app = Flask(__name__)

def random_question():
    question_info = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/question_info_data_2.csv', index_col=0)
    index = random.randint(0, question_info.shape[0])
    random_question = question_info.iloc[index]
    
    text = random_question['question_text']
    tags = random_question['keywords']
    
    return text, tags
    
@app.route('/test')
def add_numbers():
    num = 3
    return jsonify(result=num)
    
@app.route('/')
def index():
    question, keywords = random_question()
    return render_template('index.html', question=question, keywords=keywords)
    
@app.route('/model')
def model_test():
    return None
    
    
@app.route('/user/<name>')
def test_variables(name):
    return "String: %s" % name
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
