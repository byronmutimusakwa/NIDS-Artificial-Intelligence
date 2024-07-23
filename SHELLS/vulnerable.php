<?php
// Get the user input from POST
$username = $_POST['username'];

// Simulate a vulnerable SQL query (DO NOT USE IN PRODUCTION!)
$query = "SELECT * FROM users WHERE username = '$username'";

// Execute the query (not really, just simulate it)
// Vulnerable to SQL injection!
echo "Executing query: $query";
?>
