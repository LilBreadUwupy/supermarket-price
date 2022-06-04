<?php 
require "../database/database.php";
require "partials/header.php";

?>

<!-- Inside the main content -->

<div class="supermarket-h1-div" id="h1-gama">
    <h1 class="h1-type-1"> Excelsior Gama</h1>
</div>

<form action="gama.php" method="POST">
    <input type="text" name="keywords" id="keywords">
    <input type="submit" name="search" value="Buscar">
</form>

<?php

    if (isset($_POST['search'])) {
        $keywords = $_POST['keywords'];
        $keywords= explode(' ',$keywords);
        $imgs = $conn->query("SELECT * FROM products WHERE supermarket='ExcelsiorGama' AND (product LIKE '%" . $keyword . "%')");
        $len_keywords = count($keywords);
        if ($len_keywords == 1) {
            $query = "SELECT * FROM products WHERE supermarket='ExcelsiorGama' AND (product LIKE '%" . $keywords[0] . "%')";
        } else if (coun){}
        
            foreach ($keywords as $keyword ) {
                $query += 
                $imgs = $conn->query("SELECT * FROM products WHERE supermarket='ExcelsiorGama' AND (product LIKE '%" . $keyword . "%')");
            }
        
    } else {
        $imgs = $conn->query("SELECT * FROM products WHERE supermarket='ExcelsiorGama' LIMIT 105");
    } ?>

<article>
    <?php 
    foreach ($imgs as $img):?>
        <section class="section-type-1">
            <a href="<?= $img["link"] ?>" class="anchor-type-1" target="_blank">
                <h3>
                    <?= ucfirst($img["product"])?>
                </h3>
            </a>
            
            <p>
                <?= $img["price"] ?>
            </p>
            <img src="../<?= $img["img"] ?>" alt="<?= $img["product"] ?>">
        </section>
    <?php endforeach ?>
</article>

<?php require "partials/footer.php";

