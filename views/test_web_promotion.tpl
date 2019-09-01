<html>
<head>
<meta charset="UTF-8"> 
<title>Šah</title>
    <style type="text/css">
    .chessboard {
        width: 640px;
        height: 640px;
        margin: 20px;
        border: 25px solid #333;
    }
        .asdf {
        background: none;
        color: #ffffff00;
        border: none;
        padding: 0;
        font: inherit;
        cursor: pointer;
        outline: inherit;
        position: absolute;
        left: 0; 
        top: 0;
        width: 100%;
        height:100%;
    }
    .black {
        float: left;
        width: 80px;
        height: 80px;
        background-color: #999;
        font-size: 50px;
        text-align: center;
        display: table-cell;
        vertical-align: middle;
        position: relative;
    }
    .white {
        float: left;
        width: 80px;
        height: 80px;
        background-color: #fff;
        font-size: 50px;
        text-align: center;
        display: table-cell;
        vertical-align: middle;
        position: relative;
    }
    </style>
</head>

<body>
    <form action="/promote" method="POST">
    
        <div class="black">&#9813;<input class="asdf" name="i" type="submit" value="Q"></input></div>
        <div class="black">&#9814;<input class="asdf" name="i" type="submit" value="R"></input></div>
        <div class="black">&#9815;<input class="asdf" name="i" type="submit" value="B"></input></div>
        <div class="black">&#9816;<input class="asdf" name="i" type="submit" value="N"></input></div>

    </form>
</body>
</html>