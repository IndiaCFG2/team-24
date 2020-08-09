document.getElementById('lt').onclick = function() {
	console.log("HERE");
	var url = document.location.search;
	var params = {};
	var parser = document.createElement('a');
	parser.href = url;
	var query = parser.search.substring(1);
	var vars = query.split('&');
	for (var i = 0; i < vars.length; i++) {
		var pair = vars[i].split('=');
		params[pair[0]] = decodeURIComponent(pair[1]);
	}
	var tech = "low";
	generateURL(params.sid, params.gr, params.wk, 1, params.subj, tech).then(res => {
		console.log("Hmm");
		console.log(res);
		document.getElementById('url_1').innerHTML = res;
	});
}

document.getElementById('ht').onclick = function() {
	console.log("HERE");
	var url = document.location.search;
	var params = {};
	var parser = document.createElement('a');
	parser.href = url;
	var query = parser.search.substring(1);
	var vars = query.split('&');
	for (var i = 0; i < vars.length; i++) {
		var pair = vars[i].split('=');
		params[pair[0]] = decodeURIComponent(pair[1]);
	}
	var tech = "high";
	generateURL(params.sid, params.gr, params.wk, 1, params.subj, tech).then(res => {
		console.log("Hmm");
		console.log(res);
		document.getElementById('url_1').innerHTML = res;
	});
}

async function generateURL(id, gr, wk, day, subj, tech) { 
	console.log("yo");
	console.log(id);
	  let response = await fetch('/generateURL', {
            method: 'POST',
            body: JSON.stringify({'id': id, 'gr':gr, 'wk':wk, 'day':day, 'tech': tech, 'subj': subj})
        }); 

	  if (response.status == 200) {
	  	console.log("confirm");
	    let json = await response.json();
	    console.log("json", json);
	    return json['data'];
	  }

	  throw new Error(response.status);
}


async function getURL(id) { 
	  let response = await fetch('/getURL', {
            method: 'POST',
            body: JSON.stringify({'id': id})
        }); 

	  if (response.status == 200) {
	    let json = await response.json();
	    return json['data'];
	  }

	  throw new Error(response.status);
}
