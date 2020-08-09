// create functions for each filter (school, curriculum, grade etc)
curricul = (curr) => {
	// UPDATE CHART 1
	getNumberOfActive(curr).then(res => {
			document.getElementById('school-part').innerHTML = res;
	});
	updateDailyChart(curr);
	updateMonthlyChart(curr);
	updateGradeChart(curr);
	updateTechChart(curr);
	updateCityChart(curr);
	document.getElementById('school-part-curr').innerHTML = "CBSE";
	document.getElementById('clicks-24').innerHTML = Math.floor(Math.random() * 1000);
	schoolSelect(curr);
}

document.getElementById('select-school-button').onclick = (school) => {

}

async function schoolSelect(curr) {
	console.log("why?");
	var select =  document.getElementById('school-select');
	while ( select.childNodes.length >= 1 )
	{
     select.removeChild(select.firstChild);       
	}
	getNamesOfSchools(curr).then(res => {
		for (var v in res) {
		newOption = document.createElement('option');
    	newOption.value=res[v];
    	newOption.text=res[v];
    	 select.appendChild(newOption);
	}
	document.getElementById('selected-school').innerHTML = res[0];
});
}


async function getNamesOfSchools(board) { 
	  let response = await fetch('/getNamesOfSchools', {
            method: 'POST',
            body: JSON.stringify({'board': board})
        }); 

	  if (response.status == 200) {
	    let json = await response.json();
	    return json['data'];
	  }

	  throw new Error(response.status);
}



async function getNumberOfActive(board) { 
	  let response = await fetch('/getNumberOfActive', {
            method: 'POST',
            body: JSON.stringify({'board': board})
        }); 

	  if (response.status == 200) {
	    let json = await response.json();
	    return json['data'];
	  }

	  throw new Error(response.status);
}


async function getTechForCurriculum(board) { 
		console.log(board);
	  let response = await fetch('/getTechForCurriculum', {
            method: 'POST',
            body: JSON.stringify({'board': board})
        }); 

	  if (response.status == 200) {
	    let json = await response.json();
	    console.log(json['data']); 
	    return json['data'];
	  }

	  throw new Error(response.status);
}


async function getDailyForCurriculum(board) { 

	  let response = await fetch('/getDailyForCurriculum', {
            method: 'POST',
            body: JSON.stringify({'board': board})
        }); 

	  if (response.status == 200) {
	    let json = await response.json();

	    return json['data'];
	  }

	  throw new Error(response.status);
}


async function getMonthlyForCurriculum(board) { 
	  let response = await fetch('/getMonthlyForCurriculum', {
            method: 'POST',
            body: JSON.stringify({'board': board})
        }); 

	  if (response.status == 200) {
	    let json = await response.json();
	    return json['data'];
	  }

	  throw new Error(response.status);
}

async function getGradeForCurriculum(board) { 
	  let response = await fetch('/getGradeForCurriculum', {
            method: 'POST',
            body: JSON.stringify({'board': board})
        }); 

	  if (response.status == 200) {
	    let json = await response.json();
	    return json['data'];
	  }

	  throw new Error(response.status);
}

async function getCityForCurriculum(board) { 
	  let response = await fetch('/getCityForCurriculum', {
            method: 'POST',
            body: JSON.stringify({'board': board})
        }); 

	  if (response.status == 200) {
	    let json = await response.json();
	    return json['data'];
	  }

	  throw new Error(response.status);
}


updateDailyChart = (data) => {
	getDailyForCurriculum(data).then(res => {
	dataDailyClicksChart = {
        labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
        series: res
      };

      optionsDailyClicksChart = {
        lineSmooth: Chartist.Interpolation.cardinal({
          tension: 0
        }),
        low: 0,
        high: 2000, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
        chartPadding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
        },
      }

      var dailyClicksChart = new Chartist.Line('#dailyClicksChart', dataDailyClicksChart, optionsDailyClicksChart);

      md.startAnimationForLineChart(dailyClicksChart);
});
}

updateMonthlyChart = (data) => {
	getMonthlyForCurriculum(data).then(res => {
		var dataWebsiteViewsChart = {
        labels: ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'],
        series: 
          res
      };
      var optionsWebsiteViewsChart = {
        axisX: {
          showGrid: false
        },
        low: 0,
        high: 150,
        chartPadding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
        }
      };
      var responsiveOptions = [
        ['screen and (max-width: 720px)', {
          seriesBarDistance: 5,
          axisX: {
            labelInterpolationFnc: function(value) {
              return value[0];
            }
          }
        }]
      ];
      var websiteViewsChart = Chartist.Bar('#monthlyClicksChart', dataWebsiteViewsChart, optionsWebsiteViewsChart, responsiveOptions);

      //start animation for the Emails Subscription Chart
      md.startAnimationForBarChart(websiteViewsChart);
});
}

updateGradeChart = (data) => {
	getGradeForCurriculum(data).then(res => { 
		dataCompletedTasksChart = {
        labels: ['G1', 'G2', 'G3', 'G4', 'G5'],
        series: res
      };

      optionsCompletedTasksChart = {
        lineSmooth: Chartist.Interpolation.cardinal({
          tension: 0
        }),
        low: 0,
        high: 200, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
        chartPadding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
        }
      }

      var completedTasksChart = new Chartist.Line('#gradeChart', dataCompletedTasksChart, optionsCompletedTasksChart);

      // start animation for the Completed Tasks Chart - 
            md.startAnimationForLineChart(completedTasksChart);

	});
}


updateTechChart = (data) => {
	getTechForCurriculum(data).then(res => {
	dataDailyClicksChart = { 
        labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
        series: [res['low'][0], res['high'][0]]
      };

      optionsDailyClicksChart = {
        lineSmooth: Chartist.Interpolation.cardinal({
          tension: 0
        }),
        low: 0,
        high: 350, 
        chartPadding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
        },
      }



      var dailyClicksChart = new Chartist.Line('#techChart', dataDailyClicksChart, optionsDailyClicksChart);

      md.startAnimationForLineChart(dailyClicksChart);
});
}

updateCityChart = (data) => {
	getCityForCurriculum(data).then(res => {
		console.log("city");
		console.log(res);

var data = {
  labels: res['labels'],
  series: res['res']
};

var sum = function(a, b) { return a + b };

var options = {
	lineSmooth: Chartist.Interpolation.cardinal({
          tension: 0
        }),
        low: 0,
        high: 350, 
  labelInterpolationFnc: function(value) {
    return value;
  }
};

var responsiveOptions = [
  ['screen and (min-width: 640px)', {
    chartPadding: 0,
    labelOffset: 5,
    labelDirection: 'explode',
    labelInterpolationFnc: function(value) {
    return value;
  }
  }],
  ['screen and (min-width: 1024px)', {
    labelOffset: 40,
    chartPadding: 0
  }]
];

		var dailyClicksChart = new Chartist.Pie('#cityChart', data, options, responsiveOptions);
});
}