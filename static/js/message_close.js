window.onload = function () {
    let message = $('.alert');

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
    $('.ban_time').bind('keyup mouseup', function () {
        let ban_target = event.target;
        let ban_num = parseInt(ban_target.id.replace('id_ban_time-', ''));
        let ban_button_id = 'ban_submit-' + ban_num;
        if(ban_target.value !== '') {
            $('#' + ban_button_id).prop('textContent', 'подтвердить');
        } else {
            $('#' + ban_button_id).prop('textContent', 'навсегда');
        }
        // alert(ban_time.val())
    });

    $('.btn-close').click(function () {
        message.prop('style', 'display:none');

    });
};
