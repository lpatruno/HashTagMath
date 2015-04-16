$( document ).ready(function() {
    
	$.get('/getQuestion',function(data){
		var question = data['question'];
		var keywords = data['keywords'];
		console.log(question);
		console.log(keywords);
	});
});

