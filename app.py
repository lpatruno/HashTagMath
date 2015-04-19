from flask import Flask, render_template, jsonify
import pandas as pd
import random
import ast

app = Flask(__name__)

# Global variable containing the question information
#question_info = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/question_info_data_2.csv', index_col=0)
latex_text_50_df = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/latex_text_50_results.csv', index_col=0)

def random_question():
    """
    This function picks a question from the set of questions at random to display on the website
    """
    index = random.randint(0, latex_text_50_df.shape[0])
    random_question = latex_text_50_df.iloc[index]
    
    text = random_question['question_text']
    y_true = ast.literal_eval( random_question['keywords'] )
    y_pred_latex_text_50 = ast.literal_eval( random_question['y_pred'] )
    
    return text, y_true, y_pred_latex_text_50
    
@app.route('/getQuestion')
def get_data():
    """
    This method gets called by the AJAX request for a new question
    """
    question, keywords, model_2 = random_question()
    return jsonify(question=question, keywords=keywords, model_2=model_2)
    
@app.route('/')
@app.route('/index')
def index():
    """
    Method to display the keyword predictor system
    """
    return render_template('index.html')
  
  
@app.route('/about/<index>')
def get_about_page(index):
    """
    AJAX request method to serve pages of the about presentation
    """
    template = 'about%s.html' % index
    return render_template(template);
    

@app.route('/about')
def about():
    """
    Method to display the project summary presentation
    """
    return render_template('about.html')
        
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
