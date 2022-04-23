function search(invite){ // asumming invite ID is the same one as the javascript element ID
    $.get( "/api/invite/" + invite, function( data ) {
        if(data.error != "true"){
            document.getElementById(invite).innerHTML = document.getElementById(invite).innerHTML + " - Server Name: " + data.name
            console.log("Got server name via Discord's API: " + data.name)
        }else{
            document.getElementById(invite).innerHTML = document.getElementById(invite).innerHTML + " - <strong color='red'>Invalid/Expired Invite</strong>"
            console.warn("Invalid/Expired invite (ID: " + invite + ")")
        }
    });
}