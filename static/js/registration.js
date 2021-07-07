$(document).ready(function(){
    function getCookie(c_name) {
        if(document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if(c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if(c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }

    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            }
        });
    });
});
let regData = new Object();

function sendRegData(){
    userName = (document.querySelector('#regname')).value;
    userSurname = (document.querySelector('#regsurname')).value;
    userPatronymic = (document.querySelector('#regpatronymic')).value;
    userUsername = (document.querySelector('#regusername')).value;
    userPost = (document.querySelector('#regpost')).value;
    regData['name'] = userName;
    regData['surname'] = userSurname;
    regData['patronymic'] = userPatronymic;
    regData['username'] = userUsername;
    regData['post'] = userPost;


    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/users/register/",
        data: JSON.stringify(regData),
        type: 'JSON',
        success: function(response){
            console.log(response);
        }
      });
}