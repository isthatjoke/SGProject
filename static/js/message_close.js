window.onload = function () {
    let message = $('.alert');
    let ban_time = $('#id_ban_time');

    $('.link').click(function () {
        let target = event.target;
        let link_num = parseInt(target.id.replace('link-', ''));
        if (target.textContent == 'забанить') {
            let form_id = 'form-' + link_num;
            $('#' + form_id).prop('style', 'display:inline');
        } else {
            let button_id = 'submit-' + link_num;
            $('#' + button_id).prop('style', 'display:inline');
        }});

    // ban_time.change(function () {
    //     alert(ban_time.val());
    // });
    ban_time.bind('keyup mouseup', function () {
        if(ban_time.val() !== '') {
            $('.ban-submit').prop('textContent', 'подтвердить');
        } else {
            $('.ban-submit').prop('textContent', 'навсегда');
        }
        // alert(ban_time.val())
    });

    $('.btn-close').click(function () {
        message.prop('style', 'display:none');

    });
};
