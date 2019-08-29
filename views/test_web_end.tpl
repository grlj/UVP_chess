<html>
<head>
<meta charset="UTF-8"> 
<title>Chessboard using Pure CSS and HTML</title>
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
            font-size:50px;
        text-align:center;
        display: table-cell;
        vertical-align:middle;
        position: relative;
    }
    .white {
        float: left;
        width: 80px;
        height: 80px;
        background-color: #fff;
        font-size:50px;
        text-align:center;
        display: table-cell;
        vertical-align:middle;
        position: relative;
    }
    </style>
</head>

<body>
    <div class="chessboard">
    <form action="/move" method="POST">
    <% 
    for i in playboard.board:
        if (ord(i[0]) + int(i[1]) - 1)%2:
            square_colour = "black"
        else:
            square_colour = "white"
        end
        if playboard.board[i]: 
    %>
        <div class="{{square_colour}}">&#{{playboard.board[i].encode()}}; <input class="asdf" name="i" type="submit" value="{{i}}"/></div>
    %else:
        <div class="{{square_colour}}"><input class="asdf" name="i" type="submit" value="{{i}}"/></div>
    %end
    %end
    </form>
    </div>

</body>
</html>