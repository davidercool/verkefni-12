import pymysql
conn = pymysql.connect(host='tsuts.tskoli.is', user='2201002860', passwd='mypassword', db='2201002860_vef2Verk11')
import argv
from bottle import *

def rows(cur):
    return [x for x in cur]

def check_login(a, b):
    if a.lower() == 'david' and b.lower() == 'password':
        return True
    else:
        return False
@route('/')
def login():
    return template('login.tpl')
username = request.forms.get('user')
password = request.forms.get('pass')

@route('/login', method="POST")
def do_login():
    username = request.forms.get('user')
    password = request.forms.get('pass')
    if check_login(username,password):
        response.set_cookie("account", username, secret='password')
        return "<p>Welcome! You are now logged in.</p><a href='/logout'><input type='submit' value='logout'></a><a href='/database'><input type='submit' value='Database'></a>"
    else:
        return "<p>Login failed.</p>"+template('login.tpl')

@route('/database')
def db():
    username = request.get_cookie("account", secret='password')
    if username:
        return template('choice.tpl')
    else:
        return "Þú ert ekki skráður inn."

@route('/search')
def searching():
    username = request.get_cookie("account", secret='password')
    if username:
        return "<form method='post' action='/search/'><center><h1>Search Bar</h1><input type='SearchBar' name='search' required><a href='/search/'><input type='submit' value='Search'></a></center></form>"
    else:
        return "Þú ert ekki skráður inn."

@route('/search/', method="POST")
def results():
    username = request.get_cookie("account", secret='password')
    if username:
        search = request.forms.get("search")
        result = conn.cursor()
        result.execute("SELECT * FROM bilar where skraningarnumer = " + ("'" if search is not None else "") + (search if search is not None else "'") + ("'" if search is not None else "") + ";")
        listi=rows(result)
        result.close()
        s = ""
        for x in listi:
            for y in x:
                s+=str(y) + " "
            s+="\n"
        return s+template('choice.tpl') if len(listi) > 0 else "<center><h1>ERROR 404 Nothing with this name is in our database</h1></center>"+template('choice.tpl')

    else:
        return "Þú ert ekki skráður inn."

@route('/edit')
def editorial():
    username = request.get_cookie("account", secret='password')
    if username:
        return "<form method='post' action='/edit/confirm'><center><h1>Sláðu inn column nafninu sem þú villt breyta</h1><input type='editbar' name='column' required><br><h1>Sláðu inn því sem þú villt breyta</h1><input type='editbar2' name='stak' required><br><h1>Sláðu inn nýja gagnið</h1><input type='editbar3' name='new' required><br><br><a href='/search/'><input type='submit' value='Breyta'></a></center></form>"
    else:
        return "Þú ert ekki skráður inn."

@route('/edit/confirm',method='POST')
def IGNEditor():
    username = request.get_cookie("account", secret='password')
    if username:
        editorialism = request.forms.get("column")
        stake = request.forms.get("stak")
        new = request.forms.get("new")
        editor = conn.cursor()
        editor.execute("UPDATE bilar SET " + editorialism + " = '"+ new + "' WHERE "+editorialism+" = '"+stake+"';")
        conn.commit()
        editor.close()
        return "<center>Gögnunum hafa verið breytt!</center>"+template('choice.tpl')
    else:
        return "Þú ert ekki skráður inn."
@route('/add')
def changes():
    username = request.get_cookie("account", secret='password')
    if username:
        return template('form.tpl')
    else:
        return "Þú ert ekki skráður inn."

@route('/add/confirm', method="POST")
def plzDontDropTableCars():
    username = request.get_cookie("account", secret='password')
    if username:
        plata = request.forms.get("skraningarnumer")
        tegund = request.forms.get("tegund")
        factory = request.forms.get("verksmidjunumer")
        dating = request.forms.get("skraningardagur")
        carbon = request.forms.get("co2")
        weight = request.forms.get("thingd")
        check = request.forms.get("skodun")
        stat = request.forms.get("stada")
        add = conn.cursor()
        add.execute("INSERT INTO bilar VALUES ('"+plata+"','"+tegund+"','"+factory+"','"+dating+"','"+carbon+"','"+weight+"','"+check+"','"+stat+"');")
        conn.commit()
        add.close()
        return("<center>Bíllinn þinn er kominn inn í databaseið okkar, takk fyrir hjálpina!<br><br></center>"+template('choice.tpl'))
    else:
        return "Þú ert ekki skráður inn."

@route('/del')
def exterminate():
    username = request.get_cookie("account", secret='password')
    if username:
        return "<form method='post' action='/deleted'><center><h1>Skrifaðu bílnúmer bílsins sem þú villt eyða úr gagnasafninu</h1><input type='delbar' name='delete' required><a href='/deleted'><input type='submit' value='delete'></a></center></form>"
    else:
        return "Þú ert ekki skráður inn."

@route('/deleted',method="POST")
def exterminate():
    username = request.get_cookie("account", secret='password')
    if username:
        delbar = request.forms.get("delete")
        deletion = conn.cursor()
        deletion.execute("DELETE FROM bilar WHERE skraningarnumer = '"+delbar+"';")
        conn.commit()
        deletion.close()
        return '<center>Bílnum hefur verið eytt!</center>'+template('choice.tpl')
    else:
        return "Þú ert ekki skráður inn."

@route('/logout')
def logout():
    response.set_cookie("account", "", expires=0)
    return '<p>You have been logged out</p>'
run(host='0.0.0.0', port=argv[1])
