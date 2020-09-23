
$(document).ready(function() {

	$('form').on('input', function(event) {
		// console.log($('#commentInput').val());
		$.ajax({
			data : {
				comment : $('#nameInput').val(),

				
			},
			type : 'POST',
			url : '/predict'
			
		})
		.done(function(data) {
			console.log(data);

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});
		

		event.preventDefault();

	});

});