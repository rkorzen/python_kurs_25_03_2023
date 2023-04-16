def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b=10):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Nie dziel przez zero")
    return a / b


operations = {"add": add, "sub": sub, "mul": mul, "div": div}
# operations["add"](1, 2)

def get_data():
    op = input("Podaj operację [+-/*]: ")
    a = int(input("Podaj arg a: "))
    b = int(input("Podaj arg b: "))

    return op, a, b


def kalkulator_main():
    op, a, b = get_data()
    funkcja = operations[op]
    wynik = funkcja(a, b)
    print(wynik)

    a = [
        1,
        2,
        3,
        4,
    ]


if __name__ == "__main__":
    kalkulator_main()
