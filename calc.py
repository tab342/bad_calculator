import turtle
add, mult, div = lambda *args: (__import__('functools').reduce(lambda x, y: x + y, [*args], 0) if (lambda x=iter(args): all(map(lambda y: isinstance(y, int) or isinstance(y, float), x))) else None), lambda *args: (lambda add=__import__('functools').reduce, is_num=lambda x: all(map(lambda z: isinstance(z, (int, float)), x)), loop=lambda x, y: sum([x for _ in range(int(abs(y * 10**6)))]) / 10**6 if y != 0 else 0: add(lambda x, y: loop(x, y) if y > 0 else -loop(x, -y), args, 1) if is_num(args) else None)(), lambda a, b: (lambda is_num=lambda x: isinstance(x, (int, float)), check_zero=lambda x: x == 0: (lambda div_func=lambda x, y: sum([abs(y)**-1 for _ in range(int(abs(x) * 10**6))]) / 10**6 if y != 0 else float('inf'): div_func(abs(a), abs(b)) * (1 if (a >= 0) == (b >= 0) else -1) if is_num(a) and is_num(b) and not check_zero(b) else None)())()

OPERATEURS = {
    '+': 'add',
    '*': 'mult',
    '/': 'div'
}

def transformer(expression):
    def parse_expression(expr):
        stack = []
        num = ""
        for char in expr:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    stack.append(num)
                    num = ""
                stack.append(char)
        if num:
            stack.append(num)
        
        return parse_stack(stack)

    def parse_stack(tokens):
        if len(tokens) == 1:
            return tokens[0]
        
        for op in ('+', '*', '/'):
            if op in tokens:
                index = tokens.index(op)
                left = parse_stack(tokens[:index])
                right = parse_stack(tokens[index+1:])
                return f"{OPERATEURS[op]}({left},{right})"
        if '-' in tokens:
            index = tokens.index('-')
            left = parse_stack(tokens[:index])
            right = parse_stack(tokens[index+1:])
            return f"add({left},-{right})"
    
    return parse_expression(expression)


screen = turtle.Screen()
screen.title("Calculatrice")
screen.bgcolor("lightgray")
screen.setup(width=500, height=700)
screen.tracer(4000)
oui= turtle.Turtle()
oui.hideturtle()

current_input = ""

def update_display(value):
    display.clear()
    display.write(value, align="center", font=("Arial", 28, "bold"))

display = turtle.Turtle()
display.hideturtle()
display.penup()
display.goto(0, 250)
update_display("0")

def on_button_click(label):
    global current_input
    if label == "=":
        try:
            current_input = str(eval(transformer(current_input)))
        except:
            current_input = "Erreur"
    elif label == "C":
        current_input = ""
    else:
        current_input += label
    update_display(current_input)

def create_button(x, y, color, label):
    button = turtle.Turtle()
    button.shape("square")
    button.color(color)
    button.shapesize(stretch_wid=2, stretch_len=4)
    button.penup()
    button.goto(x, y)

   

    def click_handler(x, y):
        on_button_click(label)

    button.onclick(click_handler)

button_specs = [
    (-150, 120, "lightblue", "7"), (-50, 120, "lightblue", "8"), (50, 120, "lightblue", "9"),
    (-150, 50, "lightblue", "4"), (-50, 50, "lightblue", "5"), (50, 50, "lightblue", "6"),
    (-150, -20, "lightblue", "1"), (-50, -20, "lightblue", "2"), (50, -20, "lightblue", "3"),
    (-50, -90, "lightblue", "0"), (-150, -90, "lightblue", "."), (50, -90, "orange", "="),
    (150, 120, "orange", "+"), (150, 50, "orange", "-"), (150, -20, "orange", "*"), (150, -90, "orange", "/"),
    (-150, -160, "red", "C")
]

for x, y, color, label in button_specs:
    create_button(x, y, color, label)
    screen.update()


def write(x, y, label):
    button_text = turtle.Turtle()
    button_text.hideturtle()
    button_text.penup()
    button_text.goto(x, y - 10)
    button_text.write(label, align="center", font=("Arial", 18, "bold"))

for x, y, _, label in button_specs :
    write(x, y, label)

turtle.done()
