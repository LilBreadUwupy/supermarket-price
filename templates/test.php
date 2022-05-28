<?php 

require "database.php";

$imgs = $conn->query("SELECT * FROM products WHERE supermarket=ExcelsiorGama LIMIT 5"); ?>

<?php foreach ($imgs as $img): ?>
    <div>
        <p><?= $img["product"]?></p>
        <p><?= $img["price"]?></p>
        <p><?= $img["Supermarket"]?></p>
        <img src="/<?= $img["img"]?>" alt="">
    </div>
<?php endforeach ?>
