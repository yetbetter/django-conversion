function showError (e) {
    var errors = JSON.parse(e.responseText);

    $('#currency-rate').find('.error-message').remove();

    for (var i in errors) {
        var currentInput = $('#currency-rate').find('[name=' + i + ']')
        var errorPlace = currentInput.parent();
        var item = errors[i];

        errorPlace.prepend("<label for="+i+" class='error-message'>" + item[0] + "</label>");
    }

    setTimeout( function () {
        $('.error-message').remove()
    }, 5000)
}

$('#currency-rate').on('submit', function(e) {
    e.preventDefault();

    var form = $(this)
    var action = form.attr('action')
    var method = form.attr('method')
    var data = form.serialize()

    $.ajax({
        url: action,
        type: method,
        data: data,

        success: function(data) {
            currency_short_name = $('[name=to_currency]').find(':selected').html()
            result = data.number_of_money + ' ' + currency_short_name

            $('.message').removeClass('alert-danger').addClass('alert alert-success').html(result).fadeIn()
        },

        error: function(e) {
            if (e.status == 404) {
                $('.message').removeClass('alert-success').addClass('alert alert-danger').html('Unable to exchange').fadeIn();
            } if (e.status == 500) {
                $('.message').removeClass('alert-success').addClass('alert alert-danger').html('Something went wrong').fadeIn();
            } else {
                showError(e);
            }
        },
    });
});