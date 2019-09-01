<html>
<head>
<meta charset="UTF-8"> 
<title>Šah</title>
</head>
<body>

    <% 
    if len(game_log) % 2 != 0:
        game_log.append('-')
    end
    for i in range(len(game_log) // 2):
        if game_log[i * 2][0] == 'P':
            game_log[i * 2] = game_log[i * 2][1:]
    end
        if game_log[i * 2 + 1][0] == 'P':
            game_log[i * 2 + 1] = game_log[i * 2 + 1][1:]
    end
    %>
        {{i + 1}}. {{game_log[i * 2]}}, {{game_log[i * 2 + 1]}} <br>
    %end

<form action="/new_game" method="POST">
    <input name="i" type="submit" value="Nova igra">
</form>

</body>
</html>