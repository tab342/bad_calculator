while True:
    add, mult, div = lambda *args: (__import__('functools').reduce(lambda x, y: x + y, [*args], 0) if (lambda x=iter(args): all(map(lambda y: isinstance(y, int) or isinstance(y, float), x))) else None), lambda *args: (lambda add=__import__('functools').reduce, is_num=lambda x: all(map(lambda z: isinstance(z, (int, float)), x)), loop=lambda x, y: sum([x for _ in range(int(abs(y * 10**6)))]) / 10**6 if y != 0 else 0: add(lambda x, y: loop(x, y) if y > 0 else -loop(x, -y), args, 1) if is_num(args) else None)(), lambda a, b: (lambda is_num=lambda x: isinstance(x, (int, float)), check_zero=lambda x: x == 0: (lambda div_func=lambda x, y: sum([abs(y)**-1 for _ in range(int(abs(x) * 10**6))]) / 10**6 if y != 0 else float('inf'): div_func(abs(a), abs(b)) * (1 if (a >= 0) == (b >= 0) else -1) if is_num(a) and is_num(b) and not check_zero(b) else None)())()


    match int(input('1: add,2: mult,3: pow,4: div')):
        case 1:
            print(add(float(input('a=')),float(input('b='))))
        case 2:
            print(mult(float(input('a=')),float(input('b='))))
        case 3:
            print(div(float(input('a=')),float(input('b='))))