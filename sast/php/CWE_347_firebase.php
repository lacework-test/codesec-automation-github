<?php
use Firebase\JWT\JWT;

// CWE-347: Improper Verification of Cryptographic Signature (claims decoded without verifying the signature)
$parts = explode('.', $_GET['token']);
$claims = Firebase\JWT\JWT::jsonDecode(Firebase\JWT\JWT::urlsafeB64Decode($parts[1]));
?>
