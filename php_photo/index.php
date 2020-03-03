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

        $folders = array_filter(glob('./*',GLOB_ONLYDIR));
        //var_dump($images);
        foreach($folders as $folder){
            print "<a href=\"$folder/index.php\">$folder<br>\n";
        }

        ?>
    </p>
</body>
</html>
