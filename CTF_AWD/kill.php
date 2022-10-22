<?php
while (1) {
$pid=1234;
@unlink('.index.php');
exec('kill -9 $pid');
}
?>
