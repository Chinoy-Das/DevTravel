<?php
function makeconnection()
{
    $cn = mysqli_connect("db-1", "chinoy", "chinoy", "travel");
    if (mysqli_connect_errno()) {
        echo "Failed to connect to MySQL: " . mysqli_connect_error();
    }
    return $cn;
}
?>