
document.addEventListener("DOMContentLoaded", function(e){
    console.log("post loging")
    let tinyScript =  document.createElement('script');

    tinyScript.setAttribute('src','https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js');


    document.head.appendChild(tinyScript);
    tinyScript.onload = function () {
        tinymce.init({
            selector: '#id_body'
          });
    } 

})


