<?php 
require "../database/database.php";
require "partials/header.php";
$imgs = $conn->query("SELECT * FROM products WHERE supermarket = 'ExcelsiorGama' LIMIT 105");
?>

<!-- Inside the main content -->
<main>
    <div class="supermarket-h1-div" id="h1-gama">
        <h1 class="h1-type-1"> Excelsior Gama</h1>
    </div>
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

</main>

