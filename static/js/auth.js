function createCookie(name, value, days) {
    var expires;

    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    } else {
        expires = "";
    }
    document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = encodeURIComponent(name) + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ')
            c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) === 0)
            return decodeURIComponent(c.substring(nameEQ.length, c.length));
    }
    return null;
}

function eraseCookie(name) {
    createCookie(name, "", -1);
}
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
function enter(){
    login = (document.querySelector('#authlogin')).value;
    password = (document.querySelector('#authpass')).value;
    regData['username'] = login;
    regData['password'] = password;


    $.ajax({
        type: "POST",
        contentType: 'application/json; charset=utf-8',
        url: "http://127.0.0.1:8000/users/login/",
        processData: false,
        data: JSON.stringify(regData),
        success: function(response){
            createCookie("user_firstname", response.firstname, 1);
            createCookie("user_lastname", response.lastname, 1);
            createCookie("user_type", response.user_type, 1);
            console.log(response);
            messagePlace = document.querySelector('.auth__box__error');
            if(response.message != '' && typeof response.message != "undefined"){
                messagePlace.innerHTML = response.message;
            }
            if(typeof response.status_code != "undefined"){
               window.location.replace("../../assemblies/")
            }
            //window.localStorage.setItem('name', response[''])
        }
      });

}