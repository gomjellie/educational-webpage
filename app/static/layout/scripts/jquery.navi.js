//$(".item").on("mouseover", function () {
//
//    $(this).addClass('active');
//    console.log("mouseover__");
//    //stuff to do on mouseover
//});

$(".item").on({
    mouseenter: function () {
        $(this).addClass('active');
    },
    mouseleave: function () {
        $(this).removeClass('active');
    }
});
//var nav_on = function(){
//    $(this).addClass('active');
//}
//
//var nav_off = function(){
//    $(this).}