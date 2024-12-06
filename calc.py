capcodd, capcode, capkodd, capcods, kapcod, capcot = [(-150, 120, "lightblue", "7"), (-50, 120, "lightblue", "8"), (50, 120, "lightblue", "9"),(-150, 50, "lightblue", "4"), (-50, 50, "lightblue", "5"), (50, 50, "lightblue", "6"),(-150, -20, "lightblue", "1"), (-50, -20, "lightblue", "2"), (50, -20, "lightblue", "3"),(-150, -90, "lightblue", "0"), (-50, -90, "lightblue", "."), (50, -90, "orange", "="),(150, 120, "orange", "+"), (150, 50, "orange", "-"), (150, -20, "orange", "*"), (150, -90, "orange", "/"),(-150, -160, "red", "C")], lambda *args: (__import__('functools').reduce(lambda x, y: x + y, [*args], 0) if (lambda x=iter(args): all(map(lambda y: isinstance(y, int) or isinstance(y, float), x))) else None), {'+': 'capcode','*': 'capcods','/': 'capcot'}, lambda *args: (lambda capcode=__import__('functools').reduce, capcd=lambda x: all(map(lambda z: isinstance(z, (int, float)), x)), capcud=lambda x, y: sum([x for _ in range(int(abs(y * 10**6)))]) / 10**6 if y != 0 else 0: capcode(lambda x, y: capcud(x, y) if y > 0 else -capcud(x, -y), args, 1) if capcd(args) else None)(), [1], lambda a, b: (lambda capcd=lambda x: isinstance(x, (int, float)), check_zero=lambda x: x == 0: (lambda capcot=lambda x, y: sum([abs(y)**-1 for _ in range(int(abs(x) * 10**6))]) / 10**6 if y != 0 else float('inf'): capcot(abs(a), abs(b)) * (1 if (a >= 0) == (b >= 0) else -1) if capcd(a) and capcd(b) and not check_zero(b) else None)())() #candidats: on est cap
def cabcod(cabcods):
  def capcodz(gapcod):# onDéfinit
       capchod, capcood = [], ""
       for capkood in gapcod:
            if capkood.isdigit() or capkood == '.': capcood += capkood
            else:
              if capcood: capchod.append(capcood); capcood = "";capchod.append(capkood)
       if capcood: capchod.append(capcood)#condition
       return capkoid(capchod)
  def capkoid(cacpod): #on définit
     if len(cacpod) == 1:return cacpod[0]
     for capcdo in ('+', '*', '/'):
              if capcdo in cacpod:cappod = cacpod.index(capcdo);cacod = capkoid(cacpod[:cappod]);kapkood = capkoid(cacpod[cappod+1:]);return f"{capkodd[capcdo]}({cacod},{kapkood})"
     if '-' in cacpod:cappod = cacpod.index('-');cacod = capkoid(cacpod[:cappod]);kapkood = capkoid(cacpod[cappod+1:]);return f"capcode({cacod},-{kapkood})"
  return capcodz(cabcods)
cabkood = __import__("turtle").Screen();cabkood.title("Calculatrice du Chaos");cabkood.bgcolor("black");cabkood.setup(width=500, height=700);capcoodzz = __import__("turtle").Turtle();capcoodzz.hideturtle();capcoodzz.color("white");capcoodzz.penup();capcoodzz.goto(0, 250);capcoodzz.write("0", align="center", font=("Courier", 24, "bold"));capcock = "" # haha capcock
for cappcodd in range(len(capcodd)):
      kapcodd = __import__("turtle").Turtle();kapcodd.shape("square");kapcodd.color(capcodd[cappcodd][2]);kapcodd.shapesize(stretch_wid=2, stretch_len=4);kapcodd.penup();kapcodd.goto(capcodd[cappcodd][0], capcodd[cappcodd][1])
      def clic(x, y, btn=capcodd[cappcodd][3]):
        global capcock 
        if len(capcock) < 100:
         if btn == "=":capcock = str(eval(cabcod(capcock))) #condition
         elif btn == "C":capcock = ""
         else:capcock += btn
         capcoodzz.clear();capcoodzz.write(capcock, align="center", font=("Courier", 24, "bold"))
      kapcodd.onclick(clic)
for cappcodd in range(len(capcodd)):capcob = __import__("turtle").Turtle();capcob.hideturtle();capcob.penup();capcob.goto(capcodd[cappcodd][0], capcodd[cappcodd][1] - 10);capcob.write(capcodd[cappcodd][3], align="center", font=("Arial", 16, "bold"))
for _ in kapcod:__import__("turtle").done()
#7commentaires2neurones30lignes+100cafés