<?php
  session_start();
  if ($_SERVER['REQUEST_METHOD'] === 'POST') {
      $quantity = $_POST['quantity'];
      $recipient = $_POST['recipient'];
      echo "Transfer $quantity to $recipient";
  }
?>
