'use strict';

window.onload = function () {
    // добавляем ajax-обработчик для обновления количества товара
//    var csrftoken = $("input[name=csrfmiddlewaretoken]").value;


    $('#add_comment_but').click(function(){
        let formData = new FormData();
        let csrftoken = $("[name=csrfmiddlewaretoken]").value;
        formData.append('post_id', add_comment_but.value);
        formData.append('csrfmiddlewaretoken', csrftoken);
        formData.append('textarea',  id_comment_area.value);

        console.log('ajax function');
        let target_href = event.target;
        if (target_href) {
            console.log('target_href.value: ' + target_href.value);
            console.log("------>/post/"+ parseInt(target_href.value));

            $.ajax({
                data: $('#comment_form').serialize(), // get the form data
                type: $('#comment_form').attr('method'), // GET or POST
                url: $('#comment_form').attr('action'),
//                url: "/post/" + parseInt(target_href.value) + "/comment/update/",
//                dataType: 'json',
//                data: formData,
                success: function (data) {
                    console.log('ajax get data');
                    $('.comment-reload').html(data.result);
                    console.log('ajax done');
                },
            });

        }
//                event.preventDefault();
    });
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

