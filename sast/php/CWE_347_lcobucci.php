<?php
use Lcobucci\JWT\Configuration;

// CWE-347: Improper Verification of Cryptographic Signature (validated without a SignedWith constraint)
$config = Configuration::forUnsecuredSigner();
$token = $config->parser()->parse($_GET['token']);
$validator = new Lcobucci\JWT\Validation\Validator();
$validator->assert($token, new Lcobucci\JWT\Validation\Constraint\IssuedBy('https://issuer.example.com'));
?>
