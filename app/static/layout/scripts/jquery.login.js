//
//$(function() {
//    $('#teacherlogin').click(function() {
//        //var user = $('#txtUsername').val();
//        //var pass = $('#txtPassword').val();
//        var next = window.location.search;
//        next = next.replace("?", "&");
//        data = $('#teacherForm').serialize();
//        alert(data);
//        console.log("print test");
//        console.log(data);
//        $.ajax({
//            url: '/login',
//            data: $('#teacherForm').serialize() + next,
//            type: 'POST',
//            success: function(response) {
//                console.log(response);
//            },
//            error: function(error) {
//                console.log(error);
//            }
//        });
//    });
//});
//
//$(function() {
//    $('#pupillogin').click(function() {
//        //var user = $('#txtUsername').val();
//        //var pass = $('#txtPassword').val();
//        $.ajax({
//            url: '/login',
//            data: $('#pupilForm').serialize(),
//            type: 'POST',
//            success: function(response) {
//                console.log(response);
//            },
//            error: function(error) {
//                console.log(error);
//            }
//        });
//    });
//});
