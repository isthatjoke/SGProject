'use strict';


$('#id_field2').on('change', function() {
  let value = $(this).val();
  value = $('#id_field2 option[value=' + value + ']').text();

//  alert(value);
  let tags_now = $("#tags_str").val(); //То что уже вписано в строчке
  if (tags_now == '') { //если теги не указаны, то просто добавляем
    $("#tags_str").val(value);
  } else {
        let tags_array = tags_now.split(",");
        console.log('массив тегов: ' + tags_array);
//        console.log('массив тегов: ' + tags_array[0].trim());
//        console.log('массив тегов: ' + tags_array[1].trim());
//        console.log('массив тегов: ' + tags_array[2].trim());

        //теги указаны, думаем как дописать
//        alert(tags_now.split(",") + " " + tags_now.split(",").length );
        if (tags_now.split(",").length < 5) { //если тегов задано меньше 5, то добавляем в конец списка
            //проверяем есть такой тег уже в списке или нет, если есть, то убираем его, если нет, то добавляем.
            let flag = false;
            let index = 0;
            for(let i=0; i<tags_array.length; i++){
                if (tags_array[i].trim() == value){
                flag = true; //тэг уж есть в списке
                index = i; // номер этого тега
                }
            }
            if (flag==true){
                //надо удалить тэг с индексом index
                let tmp_array = [];
                for (let i=0; i<tags_array.length;i++){
                    if (i != index) {
                        tmp_array.push(tags_array[i]);
                    }
                }
                $("#tags_str").val(tmp_array);

            } else {
                //Добавляем новый тег в конец списка
                $("#tags_str").val(tags_now + ', ' + value);
            }

        } else {
            // если тегов уже 5, то добавлялем в конец, но убираем первый (всегда должно быть 5 тегов, не больше)
            //проверяем есть такой тег уже в списке или нет, если есть, то убираем его, если нет, то добавляем.
            let flag = false;
            let index = 0;
            for(let i=0; i<tags_array.length; i++){
                if (tags_array[i].trim() == value){
                flag = true; //тэг уж есть в списке
                index = i; // номер этого тега
                }
            }
            if (flag==true){
                //надо удалить тэг с индексом index
                let tmp_array = [];
                for (let i=0; i<tags_array.length;i++){
                    if (i != index) {
                        tmp_array.push(tags_array[i]);
                    }
                }
                $("#tags_str").val(tmp_array);
            }
        }

    };
 });




