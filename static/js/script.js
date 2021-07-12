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

let sendData = new Object();

function sendDetail(){
    typeOfSend = document.querySelector('.optional__adding__title').innerHTML;
    if(typeOfSend == 'Добавление элемента'){
        elemName = (document.querySelector('#inp__name')).value;
        elemDecnum = (document.querySelector('#inp__decnum')).value;
        elemVhod = (document.querySelector('#inp__vhod')).value;
        elemType = (document.querySelector('#inp__type')).value;
        sendData['name'] = elemName;
        sendData['number'] = elemDecnum;
        sendData['type'] = elemType;
        sendData['vhod'] = elemVhod;
        $.ajax({
            url: 'http://127.0.0.1:8000/assemblies/add-data/',
            type: 'POST',
            contentType: 'application/json; charset=utf-8',
            processData: false,
            data: JSON.stringify(sendData),
            success: function(){
                askForData();
            }
        });
    };
    if(typeOfSend == 'Изменение элемента'){
        fieldEdited = 0;
        let littleAr = new Object();
        elemName = (document.querySelector('#inp__name')).value;
        elemDecnum = (document.querySelector('#inp__decnum')).value;
        elemVhod = (document.querySelector('#inp__vhod')).value;
        elemType = (document.querySelector('#inp__type')).value;
        console.log(elemType);
        if(elemName != window.tecval_name){
            fieldEdited = 1;
            littleAr['name'] = elemName;
            sendData['old_name'] = window.tecval_name;
        };
        if(elemDecnum != window.tecval_selfDec){
            littleAr['decimal_number'] = elemDecnum;
            elemDecnum = window.tecval_selfDec
        };
        if(elemVhod != window.tecval_vhod){
            littleAr['entry_number'] = elemVhod
        };
        if(elemType != window.tecval_type){
        };

        sendData['decimal_number'] = elemDecnum;
        sendData['type'] = elemType;

        sendData['fields_to_edit'] = littleAr;
        $.ajax({
            url: 'http://127.0.0.1:8000/assemblies/edit-entity/',
            type: 'POST',
            contentType: 'application/json; charset=utf-8',
            processData: false,
            data: JSON.stringify(sendData),
            success: function(){
                askForData();
            }
        });
    };
    if(typeOfSend == 'Удаление элемента'){
        elemName = (document.querySelector('#inp__name')).value;
        elemDecnum = (document.querySelector('#inp__decnum')).value;
        elemVhod = (document.querySelector('#inp__vhod')).value;
        elemType = (document.querySelector('#inp__type')).value;
        sendData['decimal_number'] = elemDecnum;
        sendData['type'] = elemType;
        $.ajax({
            url: 'http://127.0.0.1:8000/assemblies/delete-entity/',
            type: 'POST',
            contentType: 'application/json; charset=utf-8',
            processData: false,
            data: JSON.stringify(sendData),
            success: function(){
                askForData();
            }
        });
    };


}

function loadExcel(){
    $.ajax({
        url: 'http://127.0.0.1:8000/assemblies/export-to-excel/',
        type: 'GET',
        processData: false,
        success: function(response) {}
    })
}

let jDataOld = {"type": "construct", "id": "\u042f\u0418\u0423\u0428.301446.006", "name": "\u0428\u043a\u0430\u0444 \u0410\u041f\u0421-\u0426", "vhod": "", "sub": [{"type": "construct", "id": "\u042f\u0418\u0423\u0428.301318.023", "name": "\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "sub": [{"type": "detail", "id": "\u042f\u0418\u0423\u0428.735336.008", "name": "\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "detail", "id": "\u042f\u0418\u0423\u0428.735336.009", "name": "\u0421\u0442\u0435\u043d\u043a\u0430 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "detail", "id": "\u042f\u0418\u0423\u0428.745322.107", "name": "\u0411\u0430\u043b\u043a\u0430", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "detail", "id": "\u042f\u0418\u0423\u0428.745322.107-01", "name": "\u0411\u0430\u043b\u043a\u0430", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "standard_detail", "id": "", "name": "\u0412\u0438\u043d\u0442 \u041c4\u04256 DIN 7985", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "standard_detail", "id": "", "name": "\u0412\u0442\u0443\u043b\u043a\u0430 \u0437\u0430\u043f\u0440\u0435\u0441\u0441\u043e\u0432\u043e\u0447\u043d\u0430\u044f BSO-M3-6", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "standard_detail", "id": "", "name": "\u0417\u0430\u043a\u043b\u0435\u043f\u043a\u0430 \u0440\u0435\u0437\u044c\u0431\u043e\u0432\u0430\u044f \u0441\u0442\u0430\u043d\u0434. \u0431\u0443\u0440\u0442\u0438\u043a \u041c8", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}]}, {"type": "construct", "id": "\u042f\u0418\u0423\u0428.301251.077-01", "name": "\u041a\u0440\u044b\u0448\u0430", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "sub": []}, {"type": "construct", "id": "\u042f\u0418\u0423\u0428.301251.077-01", "name": "\u0414\u0432\u0435\u0440\u0446\u0430 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "sub": []}]};
// let jData = {"id": "\u042f\u0418\u0423\u0428.301446.006", "name": "\u0428\u043a\u0430\u0444 \u0410\u041f\u0421-\u0426", "vhod": NaN, "type": "assembly", "sub": [{"id": "\u042f\u0418\u0423\u0428.741224.715", "name": "\u0426\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0435\u0440\u0435\u0433\u043e\u0440\u043e\u0434\u043a\u0430 \u043f\u0440\u0430\u0432\u0430\u044f", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.745551.004", "name": "\u0421\u043a\u043e\u0431\u0430 \u0442\u044f\u0433\u0438", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.745129.001", "name": "\u0422\u044f\u0433\u0430", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.745129.001-01", "name": "\u0422\u044f\u0433\u0430", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735312.153-01", "name": "\u041f\u043e\u043b\u043a\u0430 605 \u043c\u043c", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735312.153", "name": "\u041f\u043e\u043b\u043a\u0430 605 \u043c\u043c", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735312.154", "name": "\u041f\u043e\u043b\u043a\u0430 275 \u043c\u043c", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735312.154-01", "name": "\u041f\u043e\u043b\u043a\u0430 275 \u043c\u043c", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.711141.018", "name": "\u0428\u0430\u0439\u0431\u0430", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.711141.018-01", "name": "\u0428\u0430\u0439\u0431\u0430 \u0434\u0432\u0435\u0440\u0446\u044b", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.711141.018-02", "name": "\u0428\u0430\u0439\u0431\u0430 \u0434\u0432\u0435\u0440\u0446\u044b", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.711141.018-03", "name": "\u0428\u0430\u0439\u0431\u0430 \u0434\u0432\u0435\u0440\u0446\u044b", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735336.010", "name": "\u041f\u0430\u043d\u0435\u043b\u044c \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735412.132", "name": "\u0414\u0432\u0435\u0440\u0446\u0430 115\u0445325", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735412.132-01", "name": "\u0414\u0432\u0435\u0440\u0446\u0430 195x325", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735412.132-09", "name": "\u0414\u0432\u0435\u0440\u0446\u0430 270x660", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735412.132-08", "name": "\u0414\u0432\u0435\u0440\u0446\u0430 225x660", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "detail", "sub": []}, {"id": NaN, "name": "\u0412\u0438\u043d\u0442 \u041c4\u04256 DIN 7985", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0412\u0438\u043d\u0442 \u041c4\u044510 DIN 7985", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0412\u0438\u043d\u0442 \u041c5\u044512 DIN 7985", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0413\u0430\u0439\u043a\u0430 \u041c4 \u0443\u043c.\u0440\u0430\u0437\u043c. \u043f\u043e\u0434 \u043a\u043b\u044e\u0447 DIN 936", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0428\u0410\u0419\u0411\u0410 \u04105.04.019 \u0413\u041e\u0421\u0422 6958-78", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0417\u0430\u043a\u043b\u0435\u043f\u043a\u0430 \u0432\u044b\u0442\u044f\u0436\u043d\u0430\u044f \u0441\u0438\u043d\u044f\u044f DIN 7337A 4\u04458 St (RAL5005 \"\u0421\u0438\u0433\u043d\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439\")", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0417\u0430\u043a\u043b\u0435\u043f\u043a\u0430 \u0432\u044b\u0442\u044f\u0436\u043d\u0430\u044f DIN 7337A 4\u04458 St", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0417\u0430\u043a\u043b\u0435\u043f\u043a\u0430 \u0432\u044b\u0442\u044f\u0436\u043d\u0430\u044f DIN 7337\u0412 4,8\u04458 St", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0417\u0430\u043a\u043b\u0435\u043f\u043a\u0430 \u0440\u0435\u0437\u044c\u0431\u043e\u0432\u0430\u044f \u0441 \u0443\u043c. \u0431\u0443\u0440\u0442\u0438\u043a\u043e\u043c \u041c4", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0417\u0430\u043a\u043b\u0435\u043f\u043a\u0430 \u0440\u0435\u0437\u044c\u0431\u043e\u0432\u0430\u044f \u0433\u043b\u0430\u0434\u043a\u0430\u044f \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u044b\u0439 \u0431\u0443\u0440\u0442\u0438\u043a \u041c5", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0417\u0430\u043a\u043b\u0435\u043f\u043a\u0430 \u0440\u0435\u0437\u044c\u0431\u043e\u0432\u0430\u044f \u0441\u0442\u0430\u043d\u0434. \u0431\u0443\u0440\u0442\u0438\u043a \u041c8", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0421\u0442\u043e\u0439\u043a\u0430 PCHSN4-15", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u041a\u0440\u0435\u043f\u043b\u0435\u043d\u0438\u0435 \u043c\u0430\u0433\u043d\u0438\u0442\u043d\u043e\u0435 \u0441 \u0432\u0438\u043d\u0442\u043e\u043c \u042116 (\u041c4)", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0423\u043f\u043b\u043e\u0442\u043d\u0438\u0442\u0435\u043b\u044c \u0441\u043c\u043e\u043a\u043b\u0435\u044e\u0449\u0438\u0439\u0441\u044f 3\u04458 (\u0440\u044b\u0436\u0438\u0439 \u043a\u043e\u0442), \u0432 \u043c\u0435\u0442\u0440\u0430\u0445", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "sp", "sub": []}, {"id": NaN, "name": "\u041f\u0440\u043e\u0443\u0448\u0438\u043d\u0430 \u0437\u0430\u043c\u043a\u0430 SensLock SZST-21 (\u0438\u0437 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0430 \u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u0439 \u0437\u0430\u043c\u043e\u043a SensLock SZST-21)", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "op", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.754312.010", "name": "\u0428\u0438\u043b\u044c\u0434\u0438\u043a", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "op", "sub": []}, {"id": NaN, "name": "\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u044b\u0439 \u0437\u0430\u043c\u043e\u043a SensLock SZST-21", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "op", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.301318.023", "name": "\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "assembly", "sub": [{"id": "\u042f\u0418\u0423\u0428.735336.008", "name": "\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735336.009", "name": "\u0421\u0442\u0435\u043d\u043a\u0430 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.745322.107", "name": "\u0411\u0430\u043b\u043a\u0430", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.745322.107-01", "name": "\u0411\u0430\u043b\u043a\u0430", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "type": "detail", "sub": []}, {"id": NaN, "name": "\u0412\u0438\u043d\u0442 \u041c4\u04256 DIN 7985", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0412\u0442\u0443\u043b\u043a\u0430 \u0437\u0430\u043f\u0440\u0435\u0441\u0441\u043e\u0432\u043e\u0447\u043d\u0430\u044f BSO-M3-6", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0417\u0430\u043a\u043b\u0435\u043f\u043a\u0430 \u0440\u0435\u0437\u044c\u0431\u043e\u0432\u0430\u044f \u0441\u0442\u0430\u043d\u0434. \u0431\u0443\u0440\u0442\u0438\u043a \u041c8", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "type": "sp", "sub": []}]}, {"id": "\u042f\u0418\u0423\u0428.301251.077-01", "name": "\u041a\u0440\u044b\u0448\u0430", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "assembly", "sub": [{"id": "\u042f\u0418\u0423\u0428.735332.011-01", "name": "\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043a\u0440\u044b\u0448\u0438", "vhod": "\u042f\u0418\u0423\u0428.301251.077-01", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735336.007", "name": "\u041f\u0430\u043d\u0435\u043b\u044c \u043a\u0440\u044b\u0448\u0438", "vhod": "\u042f\u0418\u0423\u0428.301251.077-01", "type": "detail", "sub": []}, {"id": "\u042f\u0418\u0423\u0428.735336.011", "name": "\u041f\u0430\u043d\u0435\u043b\u044c \u043a\u0440\u044b\u0448\u0438 \u0437\u0430\u0434\u043d\u044f\u044f", "vhod": "\u042f\u0418\u0423\u0428.301251.077-01", "type": "detail", "sub": []}, {"id": NaN, "name": "\u0412\u0442\u0443\u043b\u043a\u0430 \u0437\u0430\u043f\u0440\u0435\u0441\u0441\u043e\u0432\u043e\u0447\u043d\u0430\u044f BSO-M3-10 \u0433\u043b\u0443\u0445\u0430\u044f", "vhod": "\u042f\u0418\u0423\u0428.301251.077-01", "type": "sp", "sub": []}, {"id": NaN, "name": "\u0428\u043f\u0438\u043b\u044c\u043a\u0430 \u0437\u0430\u043f\u0440\u0435\u0441\u0441\u043e\u0432\u043e\u0447\u043d\u0430\u044f \u0420\u0415\u041c \u041c4\u044512", "vhod": "\u042f\u0418\u0423\u0428.301251.077-01", "type": "sp", "sub": []}]}, {"id": "\u042f\u0418\u0423\u0428.325519.001", "name": "\u0414\u0432\u0435\u0440\u0446\u0430 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "type": "assembly", "sub": [{"id": "\u042f\u0418\u0423\u0428.325519.001 \u042d4", "name": "\u0421\u0445\u0435\u043c\u0430 \u044d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u043d\u0430\u044f", "vhod": "\u042f\u0418\u0423\u0428.325519.001", "type": NaN, "sub": []}, {"id": "\u042f\u0418\u0423\u0428.325519.001 \u041f\u042d4", "name": "\u041f\u0435\u0440\u0435\u0447\u0435\u043d\u044c \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432", "vhod": "\u042f\u0418\u0423\u0428.325519.001", "type": NaN, "sub": []}, {"id": "\u042f\u0418\u0423\u0428.741244.086", "name": "\u041f\u043b\u0430\u043d\u043a\u0430 \u043a\u0440\u0435\u043f\u043b\u0435\u043d\u0438\u044f \u043a\u0430\u043c\u0435\u0440\u044b", "vhod": "\u042f\u0418\u0423\u0428.325519.001", "type": "detail", "sub": []}]}]}

function setButtons(){
    (document.querySelectorAll('.add__button')).forEach(function(e){
        $(e).click(function(){
            $((document.querySelectorAll('.optional__adding__item'))[3]).css({"display": "flex"});
            document.querySelector('.optional__adding__title').innerHTML = "Добавление элемента";
            vhod = $(this).parent().attr("decnumber");
            document.querySelector('.optional__adding__item__button').innerHTML = "Добавить";
           //$(document.querySelector('.optional__adding__content')).toggleClass('show');
            //sendData["parent_dec"] = (e.parentElement).getAttribute('decnumber');

            (document.querySelector('#inp__vhod')).value = vhod;
            (document.querySelector('#inp__decnum')).value = "";
            (document.querySelector('#inp__name')).value = "";
            (document.querySelector('#inp__type')).value = 0;
        })
    });
    (document.querySelectorAll('.second__parent__edit-btn')).forEach(function(e){
        $(e).click(function(){
            document.querySelector('.optional__adding__item__button').innerHTML = "Изменить";
            $((document.querySelectorAll('.optional__adding__item'))[3]).css({"display": "none"});
            document.querySelector('.optional__adding__title').innerHTML = "Изменение элемента";
            name = $(this).parent().find('.second__parent__inner__text').html();
            if( name == "undefined"){
                console.log($(this).parent().parent());
            }
            vhod = ($(this).parent().parent().parent()).attr('decnumber');
            selfDec = ($(this).parent().parent()).attr('decnumber');
            type = ($(this).parent().parent()).attr('type');
            if( type == '0'){
                (document.querySelector('#inp__type')).value = 0;
            }
            if( type == '1'){
                (document.querySelector('#inp__type')).value = 1;
            }
            if( type == '2'){
                (document.querySelector('#inp__type')).value = 2;
            }
            if( type == '3'){
                (document.querySelector('#inp__type')).value = 3;
            }

            (document.querySelector('#inp__vhod')).value = vhod;
            (document.querySelector('#inp__decnum')).value = selfDec;
            (document.querySelector('#inp__name')).value = name;

            window.tecval_vhod = vhod;
            window.tecval_selfDec = selfDec;
            window.tecval_name = name;
            window.tecval_type = type;

           //$(document.querySelector('.optional__adding__content')).toggleClass('show');
            //sendData["parent_dec"] = (e.parentElement).getAttribute('decnumber');
        })
    });
    (document.querySelectorAll('.second__parent__delete-btn')).forEach(function(e){
        $(e).click(function(){
            $((document.querySelectorAll('.optional__adding__item'))[3]).css({"display": "flex"});
            document.querySelector('.optional__adding__item__button').innerHTML = "Удалить";
            document.querySelector('.optional__adding__title').innerHTML = "Удаление элемента";
            name = $(this).parent().find('.second__parent__inner__text').html();
            if( name == "undefined"){
                console.log($(this).parent().parent());
            }
            vhod = ($(this).parent().parent().parent()).attr('decnumber');
            selfDec = ($(this).parent().parent()).attr('decnumber');
            type = ($(this).parent().parent()).attr('type');
            if( type == '0'){
                (document.querySelector('#inp__type')).value = 0;
            }
            if( type == '1'){
                (document.querySelector('#inp__type')).value = 1;
            }
            if( type == '2'){
                (document.querySelector('#inp__type')).value = 2;
            }
            if( type == '3'){
                (document.querySelector('#inp__type')).value = 3;
            }

            (document.querySelector('#inp__vhod')).value = vhod;
            (document.querySelector('#inp__decnum')).value = selfDec;
            (document.querySelector('#inp__name')).value = name;
        })
    })

}

function initData(jData){
    var newParent = document.createElement('div');
    newParent.className = "parent";
    // newParent.setAttribute("number", i);
    document.querySelector("#nav").appendChild(newParent);
    newParent.innerHTML = ''+ jData.name +'';
    newParent.setAttribute("decnumber", jData.id);
    addingData(jData, 0, newParent);
}

function askForData(){
    //let localData;

    $.ajax({
        url: 'http://127.0.0.1:8000/assemblies/show-tree/',
        type: 'GET',
        success: function(response) {
            console.log(response);
            initData(response);
            setButtons();
        },
        error: function(){
            console.log('Failed');
        }
    })
}


var recNum = 0;
function addingData(data, recN, selfInDom){    
    recNum = recN + 1;
    if(data.type == '0'){
        var addButton = document.createElement('button');
        selfInDom.appendChild(addButton);
        addButton.className = "add__button";
        addButton.innerHTML = 'Добавить элемент';
        img = document.createElement('img');
        img.setAttribute('src', '../static/img/add.svg');
        img.className = "add__button__img"
        addButton.appendChild(img);
    }
    for(i in data.sub_assembly){
        curItem = data.sub_assembly[i];
        var newSecondParent = document.createElement('div');             
        newSecondParent.className = "second__parent";
        newSecondParent.setAttribute("number", i);
        newSecondParent.setAttribute("decnumber", curItem.id);
        newSecondParent.setAttribute("type", curItem.type);
        //document.querySelector(".parent").appendChild(newSecondParent);
        selfInDom.appendChild(newSecondParent);
        newSecondParent.innerHTML = '<div class = "second__parent__inner" ><div class = "second__parent__inner__text">'+ curItem.name +'</div><button class = "second__parent__edit-btn"><img class = "second__parent__edit-btn__img" src = "../static/img/edit.png"></button><button class = "second__parent__delete-btn"><img class = "second__parent__edit-btn__img" src = "../static/img/delete.png"></button></div>';
        //newSecondParent.innerHTML = ''+ curItem.name +'';
        
        if( curItem.sub_assembly !=  ''){
            addingData(curItem, recNum, newSecondParent);
        }
        if( curItem.sub_details !=  ''){
            addingData(curItem, recNum, newSecondParent);
        }
    }
    for(i in data.sub_details){
        curItem = data.sub_details[i];
        var newSecondParent = document.createElement('div');
        newSecondParent.className = "second__parent";
        newSecondParent.setAttribute("number", i);
        newSecondParent.setAttribute("decnumber", curItem.id);
        newSecondParent.setAttribute("type", curItem.type);
        //document.querySelector(".parent").appendChild(newSecondParent);
        selfInDom.appendChild(newSecondParent);
        newSecondParent.innerHTML = '<div class = "second__parent__inner" ><div class = "second__parent__inner__text">'+ curItem.name +'</div><button class = "second__parent__edit-btn"><img class = "second__parent__edit-btn__img" src = "../static/img/edit.png"></button><button class = "second__parent__delete-btn"><img class = "second__parent__edit-btn__img" src = "../static/img/delete.png"></button></div>';
        //newSecondParent.innerHTML = ''+ curItem.name +'';
    }


}
window.onload = function(){
    askForData();

}



