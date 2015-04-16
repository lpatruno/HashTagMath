$( document ).ready(function() {
    
	$.get('/getQuestion',function(data){
		var question = data['question'];
		var keywords = data['keywords'];
		
		$('#questionText').html(question);
		
		console.log(question);
		console.log(keywords);
	});
});

