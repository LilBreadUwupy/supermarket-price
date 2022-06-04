<?php 
require "../database/database.php";
require "partials/header.php";

if (isset($_POST['search'])) {
    $keywords = $_POST['keywords'];
    $imgs = $conn->query("SELECT * FROM products WHERE supermarket = 'ExcelsiorGama' AND (product LIKE '%' . $keywords)");

    //$count_results = mysql_num_rows($query);

    // if ($count_results > 0) {

    //     echo '<h2>Se han encontrado '.$count_results.' resultados.</h2>';
    // }  else {
    //     //Si no hay registros encontrados
    //     echo '<h2>No se encuentran resultados con los criterios de búsqueda.</h2>';
    // }
}


//$imgs = $conn->query("SELECT * FROM products WHERE supermarket = 'ExcelsiorGama' LIMIT 105");

?>