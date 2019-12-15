$(document).ready(function(){
	$.ajax({
		url : "http://localhost/soundSensor/data_soundSensor.php",
		type : "GET",
		success : function(data){
			console.log(data);

			var datetime1 = [];
			var temp_record = [];
			var humid_record = [];

			for(var i in data) {
				datetime1.push(data[i].datetime1.slice(0,16));
				temp_record.push(data[i].temp);
				humid_record.push(data[i].humid);
			}

			var chartdata = {
				labels: datetime1,
				datasets: [
					{
						label: "Sound Level",
						fill: false,
						lineTension: 0,
						backgroundColor: "rgba(255, 141, 43, 1)",
						borderColor: "rgba(255, 141, 43, 1)",
						pointHoverBackgroundColor: "rgba(198, 91, 0, 1)",
						pointHoverBorderColor: "rgba(198, 91, 0, 1)",
						data: temp_record
					},
					
				]
			};

			var ctx = $("#mycanvas");

			var LineGraph = new Chart(ctx, {
				type: 'line',
				data: chartdata
			});
		},
		error : function(data) {

		}
	});
});
