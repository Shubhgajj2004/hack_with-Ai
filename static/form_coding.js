$(document).ready(function() {
    $('#form2').on('submit', function(event) {
        $.ajax({
            data : {
                name : $('#nameInput').val(),
               
            },
            type : 'POST',
            url : '/create_code/process'
        })
        .done(function(data) {
           
        
                $('#result').text(data.output).show();
                
            
        });
        event.preventDefault();
    });
});

