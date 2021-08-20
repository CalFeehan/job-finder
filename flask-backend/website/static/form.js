$(document).ready(function() {

	$('#login-form').on('submit', function(event) {

		$.ajax({

			data : {
				login_email : $('#login-email').val(),
				login_password : $('#login-password').val()
			},
			type : 'POST',
			url : '/login'
		})
		.done(function(data) {

			if (data.error) {
				$('#login-fail-alert').text(data.error).show();
			}
			else {
				window.location.replace('/dashboard');
			}
            
		});

		event.preventDefault();

	});

	$('#create-account-form').on('submit', function(event) {
		
		$.ajax({
			data : {
				create_account_email : $('#create-account-email').val(),
				create_account_password : $('#create-account-password').val(),
				create_account_confirm_password : $('#create-account-confirm-password').val()
			},
			type : 'POST',
			url : '/create-account',
		})
		.done(function(data) {

			if (data.error) {
				$('#create-account-fail-alert').text(data.error).show();
			}
			else {
				window.location.replace('/dashboard');
			}
            
		});

		event.preventDefault();

	});

});
