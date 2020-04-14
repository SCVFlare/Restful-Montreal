function formulaireJSON() {
	var i = document.getElementById("id").value
	var e = document.getElementById("etablissement").value
	var a = document.getElementById("adresse").value
	var v = document.getElementById("ville").value
	var dv = document.getElementById("date_visite").value
	var p = document.getElementById("prenom").value
	var n = document.getElementById("nom").value
	var d = document.getElementById("description").value
	
	if(i=="" || e=="" || a=="" || v=="" || dv=="" || p=="" || n=="" || d==""){
		alert("All fields must filled!");
	}
	else{
		var plainte = {
		id:parseInt(i),
		etablissement:e,
		adresse:a,
		ville:v,
		date_visite:dv,
		prenom:p,
		nom:n,
		description:d
		}
		plainte=JSON.stringify(plainte)
		console.log(plainte)
		var xhr = new XMLHttpRequest();
		xhr.open("POST", "/api/plainte", true);
		xhr.setRequestHeader("Content-Type", "application/json");
		xhr.send(plainte)
		alert("Success!")
		window.location = "/";
	}
	
}
