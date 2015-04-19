from flask import Flask, render_template, jsonify
import pandas as pd
import random
import ast

app = Flask(__name__)

# Global variable containing the question information
# TODO change this to the predicted set of questions to show off the models
question_info = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/question_info_data_2.csv', index_col=0)

def random_question():
    """
    This function picks a question from the set of questions at random to display on the website
    """
    index = random.randint(0, question_info.shape[0])
    random_question = question_info.iloc[index]
    
    text = random_question['question_text']
    tags = ast.literal_eval( random_question['keywords'] )
    
    return text, tags
    
@app.route('/getQuestion')
def get_data():
    """
    This method gets called by the AJAX request for a new question
    """
    question, keywords = random_question()
    return jsonify(question=question, keywords=keywords)
    
@app.route('/')
@app.route('/index')
def index():
    """
    Method to display the keyword predictor system
    """
    return render_template('index.html')
    

@app.route('/about')
def about():
    """
    Method to display the project summary presentation
    """
    return render_template('about.html')
        
    
@app.route('/user/<name>')
def test_variables(name):
    return "String: %s" % name
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
