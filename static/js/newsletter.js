$(document).ready(function(){
    $('form').submit(function(event){
      event.preventDefault()
      form = $("form")
      //the ajax function,that returns the json object
      $.ajax({  
        'url':'/ajax/newsletter/', //
        'type':'POST', //request type/method=>sending to db
        'data':form.serialize(), //the package being passed in the request.serialize converts the package to JSON
        'dataType':'json', //
        'success': function(data){ //success alert if the form is successfully filled
          alert(data['success'])
        },
      })// END of Ajax method
      $('#id_your_name').val('')
      $("#id_email").val('')
      }) // End of submit event
    
  }) // End of document ready function
  