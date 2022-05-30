<?php

$host = "localhost";
$user = "root";
$password = "";
$database = "supermarketdb";

try {
    $conn = new PDO("mysql:host=$host;dbname=$database", $user, $password);
} catch (PDOexception $e){
    die("PDO Connection Error: " . $e ->getMessage());
}