<!DOCTYPE HTML>
<html>
    <head>
    </head>
    <body><center>
            <form action="/add/confirm", method='POST'>
            Bílnúmer<br>
            <input type="text" name="skraningarnumer" required><br><br>
            Tegund (og litur í sviga)<br>
            <input type="text" name="tegund" required><br><br>
            Verksmidjunúmer<br>
            <input type="text" name="verksmidjunumer" required><br><br>
            Skráningardagur YYYY-MM-DD<br>
            <input type="date" name="skraningardagur" placeholder="YYYY-MM-DD" required><br><br>
            co2 losun<br>
            <input type="text" name="co2" required><br><br>
            Þyngd<br>
            <input type="text" name="thingd" required><br><br>
            Næsti Skodunardagur YYYY-MM-DD<br>
            <input type="date" name="skodun" placeholder="YYYY-MM-DD" required><br><br>
            Staða bíls<br>
            <input type="text" name="stada" required><br><br>
            <a href="/add/confirm"><input type="submit" value="breyta"></a>
            </center>
        </form>
    </body>
</html>