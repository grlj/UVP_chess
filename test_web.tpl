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
    .black {
        float: left;
        width: 80px;
        height: 80px;
        background-color: #999;
            font-size:50px;
        text-align:center;
        display: table-cell;
        vertical-align:middle;
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
    }
    </style>
</head>

<body>
    <div class="chessboard">
    <% 
    for i in playboard.board:
        if (ord(i[0]) + int(i[1]) - 1)%2:
            square_colour = "black"
        else:
            square_colour = "white"
        end
        print(ord(i[0]) + int(i[1]) - 1)
        if playboard.board[i]: 
    %>
        <div class="{{square_colour}}">&#{{playboard.board[i].encode()}};</div>
    %else:
        <div class="{{square_colour}}"></div>
    %end
    %end
</div>

<form action="/move" method="POST">
    <input type="text" name="start" />
    <input type="text" name="end" />
    <input type="submit" value="move" />
</form>

</body>
</html>