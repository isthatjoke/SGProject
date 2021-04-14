'use strict';

console.log("karma.js загружен!");


// нажание пальца вниз
// находим элемент и навешиваем обработчики событий для изменения цвета иконки

let tag=document.getElementById('likes_down');
    console.log(tag.childNodes[0].classList);

tag.addEventListener('mousedown', (event) => {
   tag.className== tag.childNodes[0].classList.remove('fa-thumbs-o-down');
   tag.className== tag.childNodes[0].classList.add('fa-thumbs-down');
});
tag.addEventListener('mouseup', (event) => {
   tag.className== tag.childNodes[0].classList.remove('fa-thumbs-down');
   tag.className== tag.childNodes[0].classList.add('fa-thumbs-o-down');
   ajax_karma(0);
});


// нажание пальца вверх
// находим элемент и навешиваем обработчики событий для изменения цвета иконки
let tag2=document.getElementById('likes_up');
    console.log(tag.childNodes[0].classList);

tag2.addEventListener('mousedown', (event) => {
   tag2.className== tag2.childNodes[0].classList.remove('fa-thumbs-o-up');
   tag2.className== tag2.childNodes[0].classList.add('fa-thumbs-up');
});
tag2.addEventListener('mouseup', (event) => {
   tag2.className== tag2.childNodes[0].classList.remove('fa-thumbs-up');
   tag2.className== tag2.childNodes[0].classList.add('fa-thumbs-o-up');
   ajax_karma(1);
});



function ajax_karma(sign) {
            $.ajax({
                url: "karma/" + sign + "/",

                success: function (data) {
//                    $('.post__statistic').html(data.result);
                    $('.post__karma__count').html(data.result);
                    console.log('ajax done');
                },
            });
}




