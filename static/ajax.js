function search(invite){
    $.get( "/api/invite/" + invite, function( data ) {
        if(data.error != "true"){
            alert(data.name)
        }else{
            alert("Invalid/Expired invite")
        }
    });
}