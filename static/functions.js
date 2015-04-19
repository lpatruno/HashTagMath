function get_question(){
	
	$.get('/getQuestion', function(data){
		var question = data['question'];
		var keywords = data['keywords'];
		var keyword_string = '';
		
		for(var i=0; i<keywords.length; i++){
			keyword_string += ' <code>' + keywords[i] + '</code> ';
		}
		keyword_string += '<br>'
		
		$('#questionText').html(question);
		$('#keywords').html(keyword_string);
		
		// Render all LaTeX content
		MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
	});
}

$( document ).ready(function() {
    
	get_question();
	
	$('#newQuestion').click(function(){get_question();})
	
});

