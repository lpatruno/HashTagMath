from flask import Flask, render_template, jsonify
import pandas as pd
import random
import ast

app = Flask(__name__)

question_info = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/question_info_data_2.csv', index_col=0)

def random_question():
    #question_info = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/question_info_data_2.csv', index_col=0)
    index = random.randint(0, question_info.shape[0])
    random_question = question_info.iloc[index]
    
    text = random_question['question_text']
    tags = ast.literal_eval( random_question['keywords'] )
    
    return text, tags
    
@app.route('/getQuestion')
def get_data():
    question, keywords = random_question()
    #keywords = ast.literal_eval( keywords )
    return jsonify(question=question, keywords=keywords)
    
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
