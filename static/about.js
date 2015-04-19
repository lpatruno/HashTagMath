function get_about_page( index ){
	
	url = '/about/' + String(index);
	
	$.get(url, function(data){
		
		$('#container').html(data);
		
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

