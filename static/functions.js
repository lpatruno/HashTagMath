function get_question(){
	
	$.get('/getQuestion', function(data){
		var question = data['question'];
		var keywords = data['keywords'];
		var model_2 = data['model_2'];
		
		var keyword_string = '';
		var model_2_string ='';
		
		for(var i=0; i<keywords.length; i++){
			keyword_string += ' <code>' + keywords[i] + '</code> ';
		}
		keyword_string += '<br>'
		
		for(var i=0; i<model_2.length; i++){
			model_2_string += ' <code>' + model_2[i] + '</code> ';
		}
		model_2_string += '<br>'
		
		
		$('#questionText').html(question);
		$('#keywords').html(keyword_string);
		$('#model_2').html(model_2_string);
		
		// Render all LaTeX content
		MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
	});
}

$( document ).ready(function() {
    
	get_question();
	
	$('#newQuestion').click(function(){get_question();})
	
});

