
document.addEventListener("DOMContentLoaded", function(e){
    console.log("post loging")
    let tinyScript =  document.createElement('script');

    tinyScript.setAttribute('src','https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js');


    document.head.appendChild(tinyScript);
    tinyScript.onload = function () {
        tinymce.init({
            selector: '#id_body',
            plugins: 'codesample code',
            codesample_languages: [
                {text: 'HTML/XML', value: 'markup'},
                {text: 'JavaScript', value: 'javascript'},
                {text: 'CSS', value: 'css'},
                {text: 'PHP', value: 'php'},
                {text: 'Ruby', value: 'ruby'},
                {text: 'Python', value: 'python'},
                {text: 'Java', value: 'java'},
                {text: 'C', value: 'c'},
                {text: 'C#', value: 'csharp'},
                {text: 'C++', value: 'cpp'}
              ],
              toolbar: 'codesample code',
          });
    } 

})


