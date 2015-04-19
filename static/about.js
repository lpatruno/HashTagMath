function get_about_page( index ){
	
	url = '/getAbout/' + String(index);
	
	console.log(String(index));
	
	$.get(url, function(data){
		
		console.log(data);
		i = i + 1;
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
	
	$('#next').click(function(){get_about_page(i);})
	$('#back').click(function(){get_about_page(i-2);})
	
});

