<?php
  session_start();
  if ($_SERVER['REQUEST_METHOD'] === 'POST') {
      if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
          $quantity = $_POST['quantity'];
          $recipient = $_POST['recipient'];
	  echo "Transfer $quantity to $recipient";
      }
  }
?>
