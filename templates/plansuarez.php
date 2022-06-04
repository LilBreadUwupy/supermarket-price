<?php 
require "../database/database.php";
require "partials/header.php";
$imgs = $conn->query("SELECT * FROM products WHERE supermarket='Planzuarez' LIMIT 105");
?>


    <div class="supermarket-h1-div" id="h1-plansuarez">
        <h1> Plansuarez </h1>
    </div>

    <article>
        <?php
        foreach($imgs as $img):?>
            <section class="section-type-1">
                <h3>
                    <?= $img["product"]?>
                </h3>
                <p>
                    <?= $img["price"] ?>
                </p>
                <img src="../<?=$img["img"] ?>" alt="<?= $img["product"] ?>">
            </section>
    <?php endforeach ?>
    </article>

<?php require "partials/footer.php";
