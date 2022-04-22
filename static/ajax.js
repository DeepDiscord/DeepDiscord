function search(invite){
    $.get( "/api/invite/" + invite, function( data ) {
        alert(data);
    });
}