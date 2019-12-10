$(document).ready(function(){
	$.ajax({
		url : "http://localhost/temphummod/data_temphumid.php",
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
						label: "Temperature     ",
						fill: false,
						lineTension: 0,
						backgroundColor: "rgba(255, 141, 43, 1)",
						borderColor: "rgba(255, 141, 43, 1)",
						pointHoverBackgroundColor: "rgba(198, 91, 0, 1)",
						pointHoverBorderColor: "rgba(198, 91, 0, 1)",
						data: temp_record
					},
					{
						label: "Humidity",
						fill: false,
						lineTension: 0,
						backgroundColor: "rgba(29, 202, 255, 1)",
						borderColor: "rgba(29, 202, 255, 1)",
						pointHoverBackgroundColor: "rgba(0, 100, 131, 1)",
						pointHoverBorderColor: "rgba(0, 100, 131, 1)",
						data: humid_record
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
