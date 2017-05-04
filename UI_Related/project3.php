<?php

/*if (($handle = fopen("trialInput2.csv", "r")) !== FALSE) {
	$scores = array();
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        array_push($scores, $data);
    }
    print_r(json_encode($scores));
    fclose($handle);
}*/
$file = $_GET['username'];
echo $file;
$file = $file . ".csv";
if (($handle = fopen($file, "r")) !== FALSE) {
	$scores = "";
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
    	 $str = implode(",", $data);
    	$scores = $scores . $str . "\n";
    	
    }
    echo $scores;
    
    fclose($handle);
}
?>
