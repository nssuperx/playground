<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>photo</title>
</head>
<body>
    <p>
        <?php

        $images = array_filter(glob('{*jpg,*.jpeg,*.png}',GLOB_BRACE));
        //var_dump($images);
        foreach($images as $image){
            print "<img src=\"$image\"><br>\n";
        }

        ?>
    </p>
</body>
</html>
