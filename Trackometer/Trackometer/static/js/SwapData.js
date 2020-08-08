// create functions for each filter (school, curriculum, grade etc)

func = (curr) => {
	// do some database stuff to get
	// based on curriculum change the data
	// connect to django -> db -> give me some data
	console.log(curr);
	document.getElementById('school-part').innerHTML = "50";
	document.getElementById('school-part-curr').innerHTML = "CBSE";
	document.getElementById('clicks-24').innerHTML = "558";
	document.getElementById('selected-school').innerHTML = "Some School";
}

window.onload = func('cbse');
