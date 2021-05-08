'use strict';

//window.onload = function () {
//    // добавляем ajax-обработчик для обновления количества товара
////    var csrftoken = $("input[name=csrfmiddlewaretoken]").value;

function ajax_comment(){
console.log('ajax_comment');
//    $('#add_comment_but').click(function(){
        event.preventDefault();

        let target_href = event.target;
        if (target_href) {

            $.ajax({
                data: $('#comment_form').serialize(), // get the form data
                type: $('#comment_form').attr('method'), // GET or POST
                url: $('#comment_form').attr('action'),
                dataType: "json",
//                contentType: 'application/json; charset=utf-8',
                }).done(
                function (data) {
                    console.log('ajax get data');
                    $('.comment-reload').html(data.result);
                    $('.footer-update').removeClass('fixed-bottom');
                    let item = document.getElementsByClassName('row-comment');
                    style_update(item);
//                    $('.footer-update').addClass('fixed-bottom');
                    console.log('ajax done');

                });

//            $.ajax({
//                data: $('#comment_form').serialize(), // get the form data
//                type: $('#comment_form').attr('method'), // GET or POST
//                url: $('#comment_form').attr('action'),
//                dataType: "json",
//
//                success: function (data) {
//                    console.log('ajax get data');
//                    $('.comment-reload').html(data.result);
//                    let item = document.getElementsByClassName('row-comment');
//                    style_update(item);
//                    console.log('ajax done');
//                },
//                crossDomain: false
//            });

        }

//    });
}


function show_comments_form(parent_comment_id)
{
    if (parent_comment_id == 'write_comment')
    {
        $("#id_parent_comment").val('')
    }
    else
    {
        $("#id_parent_comment").val(parent_comment_id);
    }
    $("#comment_form").insertAfter("#" + parent_comment_id);
}

let item = document.getElementsByClassName('row-comment');


function style_update(item) {
    var flag = true;
for (var key in item) {

    if (isNaN(key) == false) {
        if(flag == true) {
        item[key].style.cssText = 'background: #f8f9fa !important; color: #000; padding: 12px; border-radius: 8px;';
        flag = false;
        } else {
        item[key].style.cssText = "background: rgb(222 232 238); \
                                   color: #000000; \
                                   padding: 12px; \
                                   border-radius: 8px;"
//                                    \
//                                   margin: 1rem 1rem;"
        flag = true;
        }
    }

  console.log(key);
}

}

style_update(item);

