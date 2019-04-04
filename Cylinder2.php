<html>
<body>
<?php

function calcvolume($r,$h) {
	$pi = 3.14;
	$volume = 2 * $pi * $r *($r + $h);
	echo "The volume is ", $volume, " m3";
}

calcvolume($_POST['radius'],$_POST['height']);
?>
</body>	

</html>