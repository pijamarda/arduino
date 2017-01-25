
$( document ).ready(function() {
    $("#add_temp_test").click(function() {
            console.log("refresco");
            //location.reload();
            $.get('api/add_temp_test/', function(data){
                console.log(data);
                var html_string = "<tr><td>" + data.fecha + "</td><td>" + data.temperatura + "</td></tr>"
                $("#t_temp tr:last").after(html_string);
            });
    });
    
});