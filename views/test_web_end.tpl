<html>
<head>
<meta charset="UTF-8"> 
<title>Šah</title>
   <link rel='stylesheet' type='text/css' href='/static/main_page.css'>
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