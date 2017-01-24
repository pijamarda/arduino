
$( document ).ready(function() {
    $("#add_temp_test").click(function() {
            console.log("refresco");
            //location.reload();
            $.get('api/add_temp_test/', function(data){
                console.log(data);
            });
    });
    
});