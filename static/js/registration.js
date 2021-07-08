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
    userEmail = (document.querySelector('#regemail')).value;
    userPhone = (document.querySelector('#regphone')).value;
    userDep = (document.querySelector('#regphone')).value;
    userBday = (document.querySelector('#regbday')).value;
    userPersNum = (document.querySelector('#regpersonalnumber')).value;
    userUsername = (document.querySelector('#regusername')).value;
    userPassword = (document.querySelector('#regpass')).value;
    userPost = (document.querySelector('#regpost')).value;
    regData['firstname'] = userName;
    regData['lastname'] = userSurname;
    regData['middlename'] = userPatronymic;
    regData['email'] = userEmail;
    regData['username'] = userUsername;
    regData['password'] = userPassword;
    regData['user_type'] = userPost;
    regData['phone_number'] = userPhone;
    regData['birth_date'] = userBday;
    regData['department'] = userDep;
    regData['personnel_number'] = userPersNum;

    $.ajax({
    url: 'http://127.0.0.1:8000/users/register/',
    type: 'POST',
    contentType: 'application/json; charset=utf-8',
    processData: false,
    data: JSON.stringify(regData),
    });

}