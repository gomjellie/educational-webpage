
$(function() {
    $('#teacherlogin').click(function() {
        //var user = $('#txtUsername').val();
        //var pass = $('#txtPassword').val();
        $.ajax({
            url: '/login',
            data: $('#teacherForm').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

$(function() {
    $('#pupillogin').click(function() {
        //var user = $('#txtUsername').val();
        //var pass = $('#txtPassword').val();
        $.ajax({
            url: '/login',
            data: $('#pupilForm').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
