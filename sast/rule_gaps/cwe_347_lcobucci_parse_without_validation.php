<?php
use Lcobucci\JWT\Configuration;

// CWE-347 gap (COD-7394): token parsed and its claims used without any validation
$config = Configuration::forUnsecuredSigner();
$token = $config->parser()->parse($_GET['token']);
if ($token->claims()->get('role') === 'admin') {
    grant_admin_access();
}
?>
