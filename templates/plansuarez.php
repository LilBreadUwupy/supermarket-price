<?php 
require "../database/database.php";
require "partials/header.php";
?>

<!-- Inside the main content -->


<!-- Div title  -->
<div class="supermarket-h1-div" id="h1-plazas">
    <h1 class="h1-type-1"> Excelsior Gama</h1>
</div>

<!-- End Div title -->


<!-- Search Bar -->

<form action="gama.php" method="POST" class="form-type-1">
<?php
    if (isset($_POST['search'])) {
        $keywords = $_POST['keywords'];?> 
        <div class="form-h1-div">
            <h1>Resultados para <span id="keyword"> <?=$keywords ?> </span> </h1>
        </div> <?php
    } else { ?>
        <div class="form-h1-div">
            <h1> Todos los productos de <span id="keyword"> Excelsior Gama </span> </h1>
        </div> <?php
    } ?>
    <input class="input-text" type="text" name="keywords" id="keywords" placeholder="Buscar Productos..." required >
    <input type="submit" name="search" value="Search" class="submit-text">
</form>

<!-- End search bar -->

<?php
    if (isset($_POST['search'])) {
        $keywords= $_POST['keywords'];
        $products = $conn->query("SELECT * FROM products WHERE supermarket='AutomercadoPlazas' AND (product LIKE '%" . $keywords . "%') ORDER BY id asc");
    } else {
        $products = $conn->query("SELECT * FROM products WHERE supermarket='ExcelsiorGama'ORDER BY product asc LIMIT 105 ");
    } 
?>


    <div class="supermarket-h1-div" id="h1-plansuarez">
        <h1> Plansuarez </h1>
    </div>


<article class="article-grid">
    <?php 
   
    foreach ($products as $product):?>
        <section class="section-type-1">
            <a href="<?= $product["link"] ?>" class="anchor-type-1" target="_blank">
                <div class="div-img">
                    <img src="../<?=$product["img"] ?>" alt="<?= $product["product"] ?>">
                </div>
                <p class="p-type1">
                    <?= ucfirst($product["product"])?> <br> <?= $product["price"] ?>
                </p>  
            </a>
        </section>
    <?php endforeach ?>
</article>

<?php require "partials/footer.php";
