<?php
//setting header to json
header('Content-Type: application/json');

//database
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'pi');
define('DB_PASSWORD', 'raspberry');
define('DB_NAME', 'libhat');

//get connection
$mysqli = new mysqli(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME);

if(!$mysqli){
	die("Connection failed: " . $mysqli->error);
}

//query to get data from the table
//$query = sprintf("SELECT id, datetime1, temp, humid, sensor_id FROM temp_humid");
//$query = sprintf("SELECT * FROM temp_humid ORDER BY id DESC LIMIT 24");
$query = sprintf("SELECT * FROM temp_humid ORDER BY id DESC LIMIT 24");

//execute query
$result = $mysqli->query($query);

//loop through the returned data
$data = array();
foreach ($result as $row) {
	$data[] = $row;
}

//free memory associated with result
$result->close();

//close connection
$mysqli->close();

//now print the data
print json_encode($data);