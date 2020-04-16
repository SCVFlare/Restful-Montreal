function onChange() {
  var nom = document.getElementById("nom").value;

	document.getElementById("results").innerHTML="";
	var xhr = new XMLHttpRequest();
	xhr.responseType = 'json';
    xhr.onreadystatechange = function() {
		if (xhr.readyState === XMLHttpRequest.DONE) {
			if (xhr.status === 200) {
				results=xhr.response;
				var t=""
				for (var i =0; i<results.length; i++){
					t+="<div id='results' class='card-body'><h3>Date d'infraction</h3><p>"+results[i]["date_infraction"]+"</p><h3>Montant</h3><p>"+results[i]["montant"]+"</p><h3>Description</h3><p>"+results[i]["description"]+"</p></div><hr>";
				}
				document.getElementById("results").innerHTML += t;
            } else {
				console.log('Erreur avec le serveur');
            }
        }
	};
	xhr.open("GET", "api/infraction/"+nom, true);
	xhr.responseType = 'json';
    xhr.send();
      
}