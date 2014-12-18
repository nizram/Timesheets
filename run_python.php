<?php
//print_r($_POST);
//print "<br>";
$dept = $_POST['Department'];
$number = $_POST['PayPeriod'];
$date = $_POST['Date'];
$file = './temp/'.$_FILES['Name']['name'];

move_uploaded_file($_FILES['Name']['tmp_name'],"./temp/{$_FILES['Name']['name']}");

//print "Department Number: "
//print "Number: $number<br>";
//print "Date: $date<br>";
//print "File: $file<br>";
//print sys_get_temp_dir();
//print "<br>";
//print_r($_FILES);
//print $_FILES['userfile']['name'];

$cmd = escapeshellcmd(sprintf('./timesheets.py "%s" "%s" "%s" "%s" &2>/dev/null', $dept, $number, $date, $file));
$download_location = system($cmd);
echo "<BR><BR>";
echo sprintf("<a href='%s'>CLICK HERE TO DOWNLOAD TIMESHEET</a>", $download_location);

?>
