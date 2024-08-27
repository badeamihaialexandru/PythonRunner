$(document).ready(function(){
    $('#input-box').on('input', function() {
        var inputText = $(this).val();
        $('#display-box').text(inputText);
    });
});

$('#run-button').click(()=>{$.ajax({

    'url' : '/execute',
    'type' : 'POST',
    'data' : {
        'code' :  $('#input-box').val()
    },
    'success' : function(data) {              
        alert('Data: '+data);
    },
    'error' : function(request,error)
    {
        alert("Request: "+JSON.stringify(request));
    }
});
console.log($('#input-box').val())
})
