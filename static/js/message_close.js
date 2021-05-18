window.onload = function () {
    let message = $('.alert');

    $('.link').click(function (e) {
        let target = e.target;
        let link_num = parseInt(target.id.replace('link-', ''));
        if (target.textContent == 'забанить') {
            let form_id = 'form-' + link_num;
            $('#' + form_id).prop('style', 'display:inline');
        } else {
            let button_id = 'submit-' + link_num;
            $('#' + button_id).prop('style', 'display:inline');
        }});

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

    $('.alert-close').click(function () {
        message.prop('style', 'display:none');

    });

    $('.notif-close').click(function (e) {
        let target = e.target;
        let par = $(this).parent();
        $.ajax({
            url: target.id,
        });
        par.prop('style', 'display:none');
        let count = $('.notif-count');
        let make_count = parseInt(count[0].textContent) - 1;
        count.prop('textContent', make_count);
    });

    $('.notif-object').click(function (e) {
        let target = e.target;
        let par = $(this).parent();

        $.ajax({
            url: par[0].children[1].id,
        });
        par.prop('style', 'display:none');
        let count = $('.notif-count');
        let make_count = parseInt(count[0].textContent) - 1;
        count.prop('textContent', make_count);
    });
};
