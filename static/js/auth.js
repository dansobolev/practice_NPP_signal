(function($) {
    if (!$.setCookie) {
        $.extend({
            setCookie: function(c_name, value, exdays) {
                try {
                    if (!c_name) return false;
                    var exdate = new Date();
                    exdate.setDate(exdate.getDate() + exdays);
                    var c_value = escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
                    document.cookie = c_name + "=" + c_value;
                }
                catch(err) {
                    return false;
                };
                return true;
            }
        });
    };
    if (!$.getCookie) {
        $.extend({
            getCookie: function(c_name) {
                try {
                    var i, x, y,
                        ARRcookies = document.cookie.split(";");
                    for (i = 0; i < ARRcookies.length; i++) {
                        x = ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
                        y = ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
                        x = x.replace(/^\s+|\s+$/g,"");
                        if (x == c_name) return unescape(y);
                    };
                }
                catch(err) {
                    return false;
                };
                return false;
            }
        });
    };
})(jQuery);
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

let enterData = new Object();
function enter(){
    login = (document.querySelector('#authlogin')).value;
    password = (document.querySelector('#authpass')).value;
    enterData['login'] = login;
    enterData['pass'] = password;

    $.ajax({
        type: "POST",
        contentType: 'application/json; charset=utf-8',
        url: "http://127.0.0.1:8000/users/login/",
        processData: false,
        data: JSON.stringify(regData),
        success(function(response){
            $.setCookie("userid", response)
        })
      });

}