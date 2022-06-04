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
        printf($keywords);
        $imgs = $conn->query("SELECT * FROM products WHERE supermarket='ExcelsiorGama' AND (product LIKE '%" . $keywords . "%')");
    } else {
        $imgs = $conn->query("SELECT * FROM products WHERE supermarket='ExcelsiorGama' LIMIT 105");
    } ?>

<article>
    <?php 
    foreach ($imgs as $img):?>
        <section class="section-type-1">
            <h3>
                <?= ucfirst($img["product"])?>
            </h3>
            <p>
                <?= $img["price"] ?>
            </p>
            <img src="../<?= $img["img"] ?>" alt="<?= $img["product"] ?>">
        </section>
    <?php endforeach ?>
</article>

<?php require "partials/footer.php";

