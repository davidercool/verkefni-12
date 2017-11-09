<!DOCTYPE HTML>
<HTML>
    <head>
        <link href="./static/form.css" type="text/css" rel="stylesheet">
     </head>
    <Body>
        <div>
        <h1>Log in</h1>
        <form action="/login", method='POST'>
            Username<br>
            <input type="text" name="user" required><br><br>
            Password<br>
            <input type="password" name="pass" required><br><br>
            <a href="/login"><input type="submit" value="login"></a>
        </form>
        </div>
    </Body>
</HTML>