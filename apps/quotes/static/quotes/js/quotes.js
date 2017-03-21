console.log('before all of it')
$(document).ready(function(){
	console.log('before form submit')
	$('#select_category').text('All')
	$('#id_quote').keyup(function(){
		var value = $(this).val();
		$('#current').text("\""+value+"\"");
	})


	$('#addQuote').submit(function(e){
		console.log('inside quotes.js')
		e.preventDefault()
		$.ajax({
			url: '/quotes',
			method: 'post',
			data: $(this).serialize(),
			success: function(serverResponse){
				console.log('serverResponse')
				console.log(serverResponse)
				$('.quotes').html(serverResponse)
			}
		})
		$(this).trigger('reset')
	})

	$('.speakerButtons').on('click', 'button', function(){

		if($(this).text() === $(this).attr('class')){
			
			$('#response').text(' ~ '+$(this).text()).css('color','blue');
			$('.speakerButtons button').text('You Got it. Try another?')
		}
		else if($(this).text() === 'You Got it. Try another?'){
			$.ajax({
				url: '/speakers',
				method: 'get',
				success: function(serverResponse){
					
					$('.speakerButtons').html(serverResponse)
				}

			})
		}
		else{
			$('#response').text("Try again..").css('color', 'red');
			$(this).hide();
			
		}	
	})

	$('.categories').click(function(e){
		console.log('inside quotes.js category filter button')
		e.preventDefault()
		var selection = $(this).text()
		$.ajax({
			url: "/categories/"+$(this).attr('id'),
			method: 'get',
			success: function(serverResponse){
				$('.quotes').html(serverResponse)
				console.log('this.text for category selection')
				console.log(selection)
				$('#select_category').text(selection)
			}
		})
	})
		
})