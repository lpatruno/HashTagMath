$( document ).ready(function() {
    
	$.get('/getQuestion',function(data){
		console.log(data);
	});
});

