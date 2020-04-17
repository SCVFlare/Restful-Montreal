function countOcc(el,list){
	nb=0;
	for (var i = 0; i < list.length; i++){
		if(list[i]["etablissement"]===el){
			nb++;
		}         
	}
	return nb;
}

function onChange() {
  var champAu = document.getElementById("au").value;
  var champDu = document.getElementById("du").value;
  var today = new Date();
  if (champAu === "" || champDu === "") {
    document.getElementById("error").innerHTML="All fields must be filled!"
  } 
  else{
	  d1=new Date(champAu);
	  d2=new Date(champDu);
	  if(d1>today || d2>today){
		  document.getElementById("error").innerHTML="Invalid date!"
	  }
	  else{
		var xhr = new XMLHttpRequest();
		xhr.responseType = 'json';
        xhr.onreadystatechange = function() {
          if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
			  document.getElementById("table").innerHTML="";
			  var response = xhr.response;
			  var results=new Set();
			  for (var j =0; j<response.length; j++){
				  results.add(response[j]["etablissement"])
			  }
			  let t="<tr><td>ETABLISSEMENT</td><td>NB PLAINTES</td></tr>";
			  results.forEach(e => {
                var tr = "<tr>";
                tr += "<td>"+e+"</td>";
                tr += "<td>"+countOcc(e,response)+"</td>";
                tr += "</tr>";
                t += tr;
              });
			  results.clear();
			  document.getElementById("table").innerHTML += t;
			  t="";
            } else {
              console.log('Erreur avec le serveur');
            }
          }
		};
		xhr.open("GET", "/api/contrevenant?du="+champDu+"&au="+champAu, true);
		xhr.responseType = 'json';
        xhr.send();
      }
  }
}
