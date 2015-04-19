from flask import Flask, render_template, jsonify
import pandas as pd
import random
import ast

app = Flask(__name__)

# Global variable containing the question information
#question_info = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/question_info_data_2.csv', index_col=0)
tag_df = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/tag_info_data_2.csv', index_col=0)
latex_text_40_df = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/latex_text_40_results.csv', index_col=0)
#latex_text_50_df = pd.read_csv('/home/vagrant/datacourse/MathQuestionTagging/data/latex_text_50_results.csv', index_col=0)


def random_question():
    """
    This function picks a question from the set of questions at random to display on the website
    """
    index = random.randint(0, latex_text_40_df.shape[0])
    random_question = latex_text_40_df.iloc[index]
    
    text = random_question['question_text']
    y_true = ast.literal_eval( random_question['keywords'] )
    y_pred_latex_text_40 = ast.literal_eval( random_question['y_pred'] )
    
    return text, y_true, y_pred_latex_text_40
    
    
def top_latex_tokens(keyword):
        """
        This function accepts a keyword and returns a pandas dataframe of the
        LaTeX tokens extracted for questions containing that keyword sorted
        by the number of times the tokens occur across all questions
        @params
            - keyword: python string for particular keyword
        """
        # Get index of row containing keyword
        index = tag_df[ tag_df['keyword'] == keyword].index[0]

        # Extract LaTeX tokens and counts
        latex_dict = ast.literal_eval( tag_df.iloc[index]['latex_tokens'] )

        # Put information in pandas DataFrame for quick sorting
        tokens = latex_dict.keys()
        count = []
        for token in tokens:
            count.append( latex_dict[token] )

        token_df = pd.DataFrame({'token' : tokens, 'count' :  count})
        token_df = token_df.sort('count', ascending=False).head(20)
        
        return token_df['token'].values
        
            
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
    
  
@app.route('/latex/<keyword>')
def get_top_latex_tokens(keyword):
    """
    AJAX method to return top LaTeX tokens associated with a particular keyword
    """
    tokens = top_latex_tokens(keyword)
    return jsonify(tokens=tokens)
    
  
@app.route('/about/<index>')
def get_about_page(index):
    """
    AJAX request method to serve pages of the about presentation
    """
    template = 'about%s.html' % index    
    
    if index == '4':
        top_tags = tag_df.sort('count', ascending=False).head(30)['keyword'].values
        return render_template(template, keywords=top_tags)
        
    return render_template(template);
    

@app.route('/about')
def about():
    """
    Method to display the project summary presentation
    """
    return render_template('about.html')
        
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
