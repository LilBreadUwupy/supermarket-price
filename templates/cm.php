<?php 
require "../database/database.php";
require "partials/header.php";
$imgs = $conn->query("SELECT * FROM products WHERE supermarket='Central Madeirense' LIMIT 105");
?>

    <div class="supermarket-h1-div" id="h1-cm">
        <h1> Central Madeirense </h1>
    </div>

    <article>
        <?php
        foreach ($imgs as $img):?>
            <section>
                <h3>
                    <?= $img["product"]?>
                </h3>
                <p> 
                    <?= $img['price']?>
                </p>
                <img src="" alt="">
            </section>
        <?php endforeach ?>
    </article>

<?php require "partials/footer.php";