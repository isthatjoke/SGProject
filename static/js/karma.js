'use strict';
console.log("karma.js загружен!");

const dislikeClasses = ['fa-thumbs-o-down', 'fa-thumbs-down'];
const likeClasses = ['fa-thumbs-o-up', 'fa-thumbs-up'];

/**
 * Функция для навешивания обработчиков на кнопки с лайками и дизлайками у поста.
 * @param element {String} id элемента, по которому осуществляется поиск на странице.
 * @param classNames {Array} массив с именами классов: первое - изначальный класс, второе - класс после нажатия кнопки.
 * @param sign {Number} "знак" кармы: 0 для дислайка, 1 для лайка.
 */
function set_event_listeners_post(element, classNames, sign) {
  let tag = document.getElementById(element);
  tag.addEventListener('mousedown', (event) => {
    tag.childNodes[0].classList.remove(classNames[0]);
    tag.childNodes[0].classList.add(classNames[1]);
  });
  tag.addEventListener('mouseup', (event) => {
    tag.childNodes[0].classList.remove(classNames[1]);
    tag.childNodes[0].classList.add(classNames[0]);
    ajax_karma(sign);
  });
}

/**
 * Функция для навешивания обработчиков на кнопки с лайками и дизлайками у комментариев. Сначала она ищет список
 * элементов по имени, а потом навешивает обработчик на каждый.
 * @param elementName {String} имя элемента, по которому осуществляется поиск на странице.
 * @param classNames {Array} массив с именами классов: первое - изначальный класс, второе - класс после нажатия кнопки.
 * @param sign {Number} "знак" кармы: 0 для дислайка, 1 для лайка.
 */
function set_event_listeners_comment(elementName, classNames, sign) {
  let tag = document.getElementsByName(elementName);
  tag.forEach(function (element) {
    element.addEventListener('mousedown', (event) => {
      element.childNodes[1].classList.remove(classNames[0]);
      element.childNodes[1].classList.add(classNames[1]);
    });
  });
  tag.forEach(function (element) {
    element.addEventListener('mouseup', (event) => {
      element.childNodes[1].classList.remove(classNames[1]);
      element.childNodes[1].classList.add(classNames[0]);
      let comment_id = Number(element.id);
      ajax_karma_comments(comment_id, sign);
    });
  });
}

// нажатие пальца вниз
set_event_listeners_post('likes_down', dislikeClasses, 0)

// нажатие пальца вверх
set_event_listeners_post('likes_up', likeClasses, 1)

// теперь всё то же самое для комментов!
// нажатие пальца вниз
set_event_listeners_comment('comment_likes_down', dislikeClasses, 0);

// нажатие пальца вверх
set_event_listeners_comment('comment_likes_up', likeClasses, 1)

/**
 * Функция отправляющая запрос со знаком кармы на контроллер кармы поста.
 * @param sign {Number} "знак" кармы: 0 для дислайка, 1 для лайка.
 */
function ajax_karma(sign) {
  $.ajax({
    url: "karma/" + sign + "/",
    success: function (data) {
      if (isNaN(data.result)) {
        $('.post__karma__msg').html(data.result);
      } else {
        $('.post__karma__count').html(data.result);
      }
    }
  });
}

/**
 * Функция отправляющая запрос со знаком кармы на контроллер кармы комментария.
 * @param comment_id {Number} id комментария, по карме которого сделали клик.
 * @param sign {Number} "знак" кармы: 0 для дислайка, 1 для лайка.
 */
function ajax_karma_comments(comment_id, sign) {
  $.ajax({
    url: "comment/" + comment_id +  "/karma/" + sign + "/",
    success: function (data) {
      if (isNaN(data.result)) {
        $('.comment__karma__msg').html(data.result);
      } else {
        $('.comment__karma__count').html(data.result);
      }
    }
  });
}


