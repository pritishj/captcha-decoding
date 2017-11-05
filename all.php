<?php
$image=array("hello-world.png", "300026.png",  "augu.jpg",    "wdgvze.png", "ofdbmf.jpg");

?>
<html>
<head>
<title>
Decoding Captchas
</title>
</head>
<body>
<?php
for($t=0;$t<5;$t++){
    $cmd="python s".($t+1).".py";
    ?>
<img src="<?php echo $image[$t]; ?>"></img>
<br><br>

<p>
<?php
echo system($cmd);
sleep(2);?>
</p><br><br>
<?php
}
?>
</body>
</html>