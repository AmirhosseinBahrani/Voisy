
function call(){
    let $ = require('jquery')
    $.ajax({
      url: "MYSCRIPT.py",
     context: document.body
    }).done(function() {
     alert('finished python script');;
    });
}