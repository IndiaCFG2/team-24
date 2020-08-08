func = (url) => {
	var params = {};
	var parser = document.createElement('a');
	parser.href = url;
	var query = parser.search.substring(1);
	var vars = query.split('&');
	for (var i = 0; i < vars.length; i++) {
		var pair = vars[i].split('=');
		params[pair[0]] = decodeURIComponent(pair[1]);
	}
	// pass schoolid to database, get curriculum var
	// for now for testing index.html?schoolid=CBSE etc
	var curriculum = "";
	if (params.schoolid === 'CBSE') {
		document.getElementById('CBSE').style.display = "block";
	}
	else if (params.schoolid === 'KTAKA') {
		document.getElementById('KTAKA').style.display = "block";
	}
	else if (params.schoolid === 'TS') {
		document.getElementById('TS').style.display = "block";
	}
	else {
		document.getElementById('MAHA').style.display = "block";
	}
}

window.onload = func(document.location.search);