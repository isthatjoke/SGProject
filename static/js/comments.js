'use strict';

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

let item = document.getElementsByClassName('row');

var flag = true;
for (var key in item) {

    if (isNaN(key) == false) {
        if(flag == true) {
        item[key].style.cssText = 'background: #79aec8; color: #fff; padding: 12px; border-radius: 8px;';
        flag = false;
        } else {
        item[key].style.cssText = 'background: #9ec6df; color: #000000; padding: 12px; border-radius: 8px;';
        flag = true;
        }
    }

  console.log(key);
}

