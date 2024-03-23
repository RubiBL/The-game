from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)


class PlayerData:
    def __init__(self):
        self.playerName = None
        self.armadura = 0
        self.health = 0
        self.healthL = 0
        self.gold = 0
        self.lvl = 0
        self.ppq = 0
        self.pm = 0
        self.pS = 0
        self.poder = 0
        self.espada1 = 0
        self.espada2 = 0
        self.espada3 = 0
        self.armadura1 = 0
        self.armadura2 = 0
        self.armadura3 = 0
        self.min = 0
        self.minijefe = 0
        self.boss = 0
        self.xpLimit = 0
        self.xp = 0
        self.enemyDamage = 0
        self.enemyHP = 0
        self.enemyHPL = 0
        self.enemy = 0
        self.turn = 0
        self.Type = 0
        self.race=0

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', p=True)


@app.route('/nombre', methods=['GET', 'POST'])
def nombre():
    playerData.playerName = request.form['nombre']
    return render_template('index.html', nombre=playerData.playerName, pp=True, p=False)


@app.route('/otro', methods=['POST'])
def otro():
    playerData.playerName = None
    return render_template('index.html', p=True, pp=False)


@app.route('/typ3', methods=['GET', 'POST'])
def typ3():
    return render_template('index.html', typ3=True, p=False, pp=False)


@app.route('/pq1', methods=['GET', 'POST'])
def pq1():
    if playerData.health==playerData.healthL:
       men="<p>You have Max health, don´t waste your potions (・へ・)<p>" 
       return render_template('index.html', inv2=True, inv=False,men=men)
    else:
       men="<p>You have use Small potion(+10% health)<p>"
       playerData.ppq-=1
       playerData.health+=(playerData.healthL/10)
       if playerData.health>=playerData.healthL:
           men+="<p>MAX health<p>"
    return render_template('index.html', inv2=True, inv=False,men=men)  

@app.route('/pm1', methods=['GET', 'POST'])
def pm1():
    if playerData.health==playerData.healthL:
       men="<p>You have Max health, don´t waste your potions (・へ・)<p>" 
       return render_template('index.html', inv2=True, inv=False,men=men)
    else:
       men="<p>You have use Medium potion(+30% health)<p>"
       playerData.pm-=1
       playerData.health+=3*(playerData.healthL/10)
       if playerData.health>=playerData.healthL:
           men+="<p>MAX health<p>"
    return render_template('index.html', inv2=True, inv=False,men=men) 

@app.route('/pS1', methods=['GET', 'POST'])
def pS1():
    if playerData.health==playerData.healthL:
       men="<p>You have Max health, don´t waste your potions (・へ・)<p>" 
       return render_template('index.html', inv2=True, inv=False,men=men)
    else:
       men="<p>You have use HOLY POTION(MAX health)<p>"
       playerData.pS-=1
       playerData.health=playerData.healthL       
       men+="<p>MAX health<p>"
    return render_template('index.html', inv2=True, inv=False,men=men) 

@app.route('/es1', methods=['GET', 'POST'])
def es1():
    men="<p>You have equipped:Kitchen Knife(+10 power)<p>"
    playerData.poder+=10
    playerData.espada1=2
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/es12', methods=['GET', 'POST'])
def es12():
    men="<p>You have unequipped:Kitchen Knife(+10 power)<p>"
    playerData.poder-=10
    playerData.espada1=1
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/es2', methods=['GET', 'POST'])
def es2():
    men="<p>You have equipped:Knight's sword(+30 power)<p>"
    playerData.poder+=30
    playerData.espada2=2
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/es22', methods=['GET', 'POST'])
def es22():
    men="<p>You have unequipped:Knight's sword(+30 power)<p>"
    playerData.poder-=30
    playerData.espada2=1
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/es3', methods=['GET', 'POST'])
def es3():
    men="<p>You have equipped:Sword of penance(+100 power)<p>"
    playerData.poder+=100
    playerData.espada3=2
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/es32', methods=['GET', 'POST'])
def es32():
    men="<p>You have unequipped:Sword of penance(+100 power)<p>"
    playerData.poder-=100
    playerData.espada3=1
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/ar1', methods=['GET', 'POST'])
def ar1():
    men="<p>You have equipped:Sarting armor (+10 armor)<p>"
    playerData.armadura+=10
    playerData.armadura1=2
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/ar12', methods=['GET', 'POST'])
def ar12():
    men="<p>You have unequipped:Sarting armor (+10 armor)<p>"
    playerData.armadura-=10
    playerData.armadura1=1
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/ar2', methods=['GET', 'POST'])
def ar2():
    men="<p>You have equipped:Knight's armor (+30 armor)<p>"
    playerData.armadura+=30
    playerData.armadura2=2
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/ar22', methods=['GET', 'POST'])
def ar22():
    men="<p>You have unequipped:Knight's armor (+30 armor)<p>"
    playerData.armadura-=30
    playerData.armadura2=1
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/ar3', methods=['GET', 'POST'])
def ar3():
    men="<p>You have equipped:Dragon cuirass armor (+70 armor)<p>"
    playerData.armadura+=70
    playerData.armadura3=2
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/es32', methods=['GET', 'POST'])
def ar32():
    men="<p>You have unequipped:Dragon cuirass armor (+70 armor)<p>"
    playerData.armadura-=70
    playerData.armadura3=1
    return render_template('index.html', inv2=True, inv=False,men=men)

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    men="<h1>Inventory<h1>"
    if playerData.ppq==0 and playerData.pm==0 and playerData.pS==0 and playerData.armadura1==0 and playerData.armadura2==0 and playerData.armadura3==0 and playerData.espada1==0 and playerData.espada2==0 and playerData.espada3==0:
        men+="<p> you have no items (-_-;)<p> "
    if playerData.ppq>0:
        men+="""
        <form action="/pq1" method="post">
        <button type="submit" name="boton">Small potion(+10% health)</button>
        </form>
        """
    elif playerData.pm>0:
        men+="""
        <form action="/pm1" method="post">
        <button type="submit" name="boton">Medium potion (+30% health)</button>
        </form>
        """
    elif playerData.pS>0:
      men+="""
      <form action="/pS1" method="post">
      <button type="submit" name="boton">DHoly potion (Max Health)</button>
      </form>
      """
    elif playerData.armadura1>0:
        if playerData.armadura1==1:
            men+="""
            <form action="/ar1" method="post">
            <button type="submit" name="boton">Equip:Sarting armor (+10 armor)</button>
            </form>
            """
        elif playerData.armadura1==2:
            men+="""
            <form action="/ar12" method="post">
            <button type="submit" name="boton">Unequip:Sarting armor (+10 armor)</button>
            </form>
            """
    elif playerData.armadura2>0:
        if playerData.armadura2==1:
            men+="""
            <form action="/ar2" method="post">
            <button type="submit" name="boton">Equip:Knight's armor (+30 armor)</button>
            </form>
            """
        elif playerData.armadura2==2:
            men+="""
            <form action="/ar22" method="post">
            <button type="submit" name="boton">Unequip:Knight's armor (+30 armor)</button>
            </form>
            """
    elif playerData.armadura3>0:
        if playerData.armadura3==1:
            men+="""
            <form action="/ar3" method="post">
            <button type="submit" name="boton">Equip:Dragon cuirass armor (+70 armor)</button>
            </form>
            """
        elif playerData.armadura3==2:
            men+="""
            <form action="/ar32" method="post">
            <button type="submit" name="boton">Unequip:Dragon cuirass armor (+70 armor)</button>
            </form>
            """
    elif playerData.espada1>0:
        if playerData.espada1==1:
            men+="""
            <form action="/es1" method="post">
            <button type="submit" name="boton">Equip:Kitchen Knife(+10 power)</button>
            </form>
            """
        elif playerData.espada1==2:
           men+="""
           <form action="/es12" method="post">
           <button type="submit" name="boton">Unequip:Kitchen Knife(+10 power)</button>
           </form>
           """ 
    elif playerData.espada2>0:
        if playerData.espada2==1:
            men+="""
            <form action="/es2" method="post">
            <button type="submit" name="boton">Equip:Knight's sword(+30 power)</button>
            </form>
            """
        elif playerData.espada2==2:
            men+="""
            <form action="/es22" method="post">
            <button type="submit" name="boton">Unequip:Knight's sword(+30 power)</button>
            </form>
            """
    elif playerData.espada3>0:
        if playerData.espada3==1:
            men+="""
            <form action="/es3" method="post">
            <button type="submit" name="boton">Equip:Sword of penance(+100 power)</button>
            </form>
            """
        elif playerData.espada3==2:
            men+="""
            <form action="/es32" method="post">
            <button type="submit" name="boton">Unequip:Sword of penance(+100 power)</button>
            </form>
            """
    return render_template('index.html', inv=True, menu=False,men=men)

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    x = request.form['tipo']
    if x == '1':
        playerData.race=1
        return render_template('index.html', typ3=False,menu=True)
    elif x == '2':
        playerData.race=2
        return render_template('index.html', typ3=False,menu=True)
    elif x == '3':
        playerData.race=3
        return render_template('index.html', typ3=False,menu=True)
    elif x=='4':
        return render_template('index.html', stats=False,menu=True)
    elif x=='5':
        return render_template('index.html', inneg=False, menu=True)
    elif x=='6':
        return render_template('index.html', inv=False, menu=True)
    elif x=='7':
        return render_template('index.html', inv2=False, inv=True)

@app.route('/pq', methods=['GET', 'POST'])
def pq():
    if playerData.gold<50:
        men="<p> ypu dont have enough gold (-_-;)<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)
    else:
        playerData.ppq+=1
        playerData.gold-=50
        men="<p>Thx for buying,come back soon<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)

@app.route('/pm', methods=['GET', 'POST'])
def pm():
    if playerData.gold<150:
        men="<p> ypu dont have enough gold (-_-;)<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)
    else:
        playerData.pm+=1
        playerData.gold-=150
        men="<p>Thx for buying,come back soon<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)

@app.route('/pS', methods=['GET', 'POST'])
def pS():
    if playerData.gold<500:
        men="<p> ypu dont have enough gold (-_-;)<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)
    else:
        playerData.pS+=1
        playerData.gold-=500
        men="<p>Thx for buying,come back soon<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)

@app.route('/a1', methods=['GET', 'POST'])
def a1():
    if playerData.gold<100:
        men="<p> ypu dont have enough gold (-_-;)<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)
    else:
        playerData.armadura1+=1
        playerData.gold-=100
        men="<p>Thx for buying,come back soon<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)

@app.route('/a2', methods=['GET', 'POST'])
def a3():
    if playerData.gold<300:
        men="<p> ypu dont have enough gold (-_-;)<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)
    else:
        playerData.armadura2+=1
        playerData.gold-=300
        men="<p>Thx for buying,come back soon<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)

@app.route('/a3', methods=['GET', 'POST'])
def a4():
    if playerData.gold<1000:
        men="<p> ypu dont have enough gold (-_-;)<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)
    else:
        playerData.armadura3+=1
        playerData.gold-=1000
        men="<p>Thx for buying,come back soon<p>"
        return render_template('index.html',ineg=True,inneg=False,men=men)
@app.route('/stats', methods=['GET', 'POST'])
def stats():
        stat = f"<p>Name: {playerData.playerName}"
        if playerData.race==1:
            race="Elf"
        if playerData.race==2:
            race="Human"
        if playerData.race==3:
            race="Hobbit"
        stat+=f"<br>Race:{race}"
        if playerData.boss == 1:
            stat += "<br>Title: Hero"
        stat += f"<br>LVL:{playerData.lvl}"
        stat += f"<br>XP:{playerData.xp}/{playerData.xpLimit}"
        stat += f"<br>Health:{playerData.health}/{playerData.healthL}"
        if playerData.espada1 == 2:
            stat += "<br>Cooking knife Equipped(+10 Power)"
        elif playerData.espada2 == 2:
            stat += "Knight's sword Equipped(+30 Power)"
        elif playerData.espada3 == 2:
            stat += "Sword of Penance Equipped(+100 Power)"
        stat += f"<br>Power:{playerData.poder}"
        p1 = playerData.poder - 10
        if playerData.espada1 < 2 and playerData.espada2 < 2 and playerData.espada3 < 2:
            p2 = playerData.poder + 10
        elif playerData.espada1 == 2:
            p2 = playerData.poder + 20
        elif playerData.espada2 == 2:
            p2 = playerData.poder + 40
        elif playerData.espada3 == 2:
            p2 = playerData.poder + 110
        stat += f"<br>Light attack:{p1}-{p2}" 
        p3 = playerData.poder + 30
        if playerData.espada1 < 2 and playerData.espada2 < 2 and playerData.espada3 < 2:
            p4 = playerData.poder + 50
        elif playerData.espada1 == 2:
            p4 = playerData.poder + 60
        elif playerData.espada2 == 2:
            p4 = playerData.poder + 80
        elif playerData.espada3 == 2:
            p4 = playerData.poder + 150
        stat += f"<br>Heavy attack:{p3}-{p4}"
        if playerData.armadura1 == 2:
            stat += "<br>Starting Armor Equipped(+10 armor)"
        elif playerData.armadura2 == 2:
            stat += "<br>Knight Armor Equipped(+30 armor)"
        elif playerData.armadura3 == 2:
            stat += "<br>Dragon Cuirass Armor Equipped(+70 armor)"
        ar=playerData.armadura
        stat+=f"<br>Armor:{ar}<br>Damage reduction:{ar}%<p>"
        return render_template('index.html', menu=False,stats=True,stat=stat)

@app.route('/store', methods=['GET', 'POST'])
def store():
        if playerData.gold<=0:
             men="<p>You have no gold ( ͠° ⏥ ͡°)<p>"
             return render_template('index.html', menu=False, inneg=True,men=men)
        if playerData.gold>0:
             text="<h1 id='texto'>Welcome to Walmart</h1>"
             text+="""
            <form action="/pq" method="post">
             <button type="submit" name="boton">Small potion +10% health(50 Gold)</button>
             </form>
             <form action="/pm" method="post">
             <button type="submit" name="boton">Medium potion +30% health(150 Gold)</button>
             </form>
             <form action="/pS" method="post">
             <button type="submit" name="boton">Holy potion Max Health(500 Gold)</button>
             </form>
             """
        if playerData.armadura1==0:
                text+="""
                <form action="/a1" method="post">
                <button type="submit" name="boton">Sarting armor +10 armor(100 Gold)</button>
                </form>
                """
        if playerData.armadura2==0:
            text+="""
            <form action="/a2" method="post">
            <button type="submit" name="boton">Knight's armor +30 armor(300 Gold)</button>
            </form>
            """
        if playerData.armadura3==0:
            text+="""
            <form action="/a3" method="post">
            <button type="submit" name="boton">Dragon cuirass armor +70 armor(1000 Gold)</button>
            </form>
            """
        return render_template('index.html',menu=False,inneg=True,men=text)


@app.route('/combat', methods=['GET', 'POST'])
def combat():
    return render_template('index.html',)


if __name__ == '__main__':
    playerData = PlayerData()
    playerData.health = 100
    playerData.poder = 20
    playerData.armadura = 10
    playerData.gold = 10
    playerData.ppq = 0
    playerData.pm = 0
    playerData.pS = 0
    playerData.espada1 = 0
    playerData.espada2 = 0
    playerData.espada3 = 0
    playerData.armadura1 = 0
    playerData.armadura2 = 0
    playerData.armadura3 = 0
    playerData.min = 0
    playerData.minijefe = 0
    playerData.boss = 0
    playerData.lvl = 1
    playerData.xp = 0
    playerData.healthL = 100
    playerData.xpLimit = 100
    app.run(debug=True)
