function get_about_page( index ){
	
	$.get('/getAbout/<index>', function(data){
		
		console.log(data);
		/*
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
		*/
		
	});
}

$( document ).ready(function() {
	
	i = 0;
    
	get_about_page(i);
	
	// TODO add a button to navigate to the next part of presentation
	//$('#newQuestion').click(function(){get_question();})
	
});

