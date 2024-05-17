<?php
session_start();
$_SESSION["username"] = "";
$_SESSION["usertype"] = "";
$_SESSION["loginstatus"] = "";

header("Location: loginform.php");
exit();
?>