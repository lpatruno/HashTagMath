function get_about_page( index ){
	
	url = '/getAbout/' + String(index);
	
	$.get(url, function(data){
		
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
	
	$('#next').click(function(){
		i = i + 1;
		get_about_page(i);
	});
	
	$('#back').click(function(){
		if (i>0){
			i = i - 1;
			get_about_page(i);
		}
	});
	
	get_about_page(i);
	
});

