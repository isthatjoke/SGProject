window.onload = function () {
    let message = $('.message');
    $('.close').click(function () {
        message.prop('style', 'display:none');
    });
};