<?php
$image=array("hello-world.png", "300026.png",  "augu.jpg",    "wdgvze.png", "ofdbmf.jpg");
$ran=rand(0,4) ;
$t=$ran+1;
$cmd="python s".$t.".py";
?>
<html>
<head>
<title>
Decoding Captchas
</title>
</head>
<body>
<img src="<?php echo $image[$ran]; ?>"></img>
<br><br>


<?php
echo "<p>".system($cmd)."</p>";
sleep(5);
?>

</body>
</html>
