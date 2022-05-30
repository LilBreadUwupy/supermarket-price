<?php 

require "../database/database.php";
require "../templates/partial/header.php";

$imgs = $conn->query("SELECT * FROM products WHERE supermarket= 'ExcelsiorGama' LIMIT 35"); ?>

<?php foreach ($imgs as $img): ?>
    <p>
        <?= $img["product"]?>
    </p>
    <p>
        <?= $img["price"]?>
    </p>
    <p>
        <?= $img["Supermarket"]?>
    </p>
    <?php printf($img["img"])?>
    <img src="../<?=$img["img"]?>" alt="">
    <a href=""></a>
<?php endforeach ?>