let jData = {"type": "construct", "id": "\u042f\u0418\u0423\u0428.301446.006", "name": "\u0428\u043a\u0430\u0444 \u0410\u041f\u0421-\u0426", "vhod": "", "sub": [{"type": "construct", "id": "\u042f\u0418\u0423\u0428.301318.023", "name": "\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "sub": [{"type": "detail", "id": "\u042f\u0418\u0423\u0428.735336.008", "name": "\u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "detail", "id": "\u042f\u0418\u0423\u0428.735336.009", "name": "\u0421\u0442\u0435\u043d\u043a\u0430 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u044f", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "detail", "id": "\u042f\u0418\u0423\u0428.745322.107", "name": "\u0411\u0430\u043b\u043a\u0430", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "detail", "id": "\u042f\u0418\u0423\u0428.745322.107-01", "name": "\u0411\u0430\u043b\u043a\u0430", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "standard_detail", "id": "", "name": "\u0412\u0438\u043d\u0442 \u041c4\u04256 DIN 7985", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "standard_detail", "id": "", "name": "\u0412\u0442\u0443\u043b\u043a\u0430 \u0437\u0430\u043f\u0440\u0435\u0441\u0441\u043e\u0432\u043e\u0447\u043d\u0430\u044f BSO-M3-6", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}, {"type": "standard_detail", "id": "", "name": "\u0417\u0430\u043a\u043b\u0435\u043f\u043a\u0430 \u0440\u0435\u0437\u044c\u0431\u043e\u0432\u0430\u044f \u0441\u0442\u0430\u043d\u0434. \u0431\u0443\u0440\u0442\u0438\u043a \u041c8", "vhod": "\u042f\u0418\u0423\u0428.301318.023", "sub": []}]}, {"type": "construct", "id": "\u042f\u0418\u0423\u0428.301251.077-01", "name": "\u041a\u0440\u044b\u0448\u0430", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "sub": []}, {"type": "construct", "id": "\u042f\u0418\u0423\u0428.301251.077-01", "name": "\u0414\u0432\u0435\u0440\u0446\u0430 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f", "vhod": "\u042f\u0418\u0423\u0428.301446.006", "sub": []}]};
// console.log(jData.type);
// console.log(jData.id);
// console.log(jData.name);
// console.log(jData.vhod);
function listing(data){
    var newParent = document.createElement('div');             
    newParent.className = "parent";
        // newParent.setAttribute("number", i);
    document.querySelector("#main").appendChild(newParent);
    newParent.innerHTML = ''+ data.name +'';
    for(i in data.sub){
        // console.log(data.sub[i]);    
        var newSecondParent = document.createElement('div');             
        newSecondParent.className = "second__parent";
        newSecondParent.setAttribute("number", i);
        newSecondParent.setAttribute("decnumber", data.sub[i].id);
        document.querySelector(".parent").appendChild(newSecondParent);
        newSecondParent.innerHTML = ''+ data.sub[i].name +'';
        //console.log(data.sub[i].sub == ''); 
        if( data.sub[i].sub != '' ){        
            // console.log("Have child");
            // console.log(data.sub[i].sub);    
            //listing(data.sub[i].sub);
            //for( data.sub[i].sub )
            let newJData = data.sub[i].sub;            
            document.querySelectorAll(".second__parent").forEach(function(e){
                if(e.getAttribute("number") == i){
                    window.localParent = e;
                    //console.log(localParent)
                }
            })            
            for(j in newJData){
                var newThirdParent = document.createElement('div');             
                newThirdParent.className = "third__parent";
                newThirdParent.setAttribute("number", j);
                console.log(newJData[j].id);
                newThirdParent.setAttribute("decnumber", newJData[j].id);
                localParent.appendChild(newThirdParent);
                newThirdParent.innerHTML = ''+ newJData[j].name +'';
                // console.log("Work");   
                console.log(newJData[j])
                // console.log(newJData.[j]);    
                //console.log(data.sub[i].sub == ''); 
                if( newJData[j].sub != '' ){  
                    // console.log("Work2");      
                    // console.log(newJData[j].sub);    
                    //listing(data.sub[i].sub);
                }
            }
        }
    }
}
listing(jData);

document.querySelectorAll(".secondParent").forEach(function(e){
    console.log(e.getAttribute("number"))
})

