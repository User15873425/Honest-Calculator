def calculator():
    try:
        x, sign, y = input(msg[0]).split()
        x = memory if x == 'M' else float(x)
        y = memory if y == 'M' else float(y)
        result = operation(x, y, sign)
    except ValueError:
        print(msg[1])
        calculator()
    except TypeError:
        print(msg[2])
        calculator()
    except ZeroDivisionError:
        print(msg[3])
        calculator()
    else:
        lazy(x, y, sign)
        print(result)
        save_in_memory(result)
        next_calc()


def is_one_digit(v):
    return v.is_integer() and -10 < v < 10


def lazy(v1, v2, v3):
    output = msg[6] if is_one_digit(v1) and is_one_digit(v2) else ''
    if (v1 == 1 or v2 == 1) and v3 == '*':
        output += msg[7]
    if v1 == 0 or v2 == 0 and v3 in ['*', '+', '-']:
        output += msg[8]
    if output != '':
        print(msg[9] + output)


def next_calc():
    answer = input(msg[5])
    if answer == 'y':
        calculator()
    elif answer != 'n':
        next_calc()


def operation(v1, v2, v3):
    if v3 == '+':
        return v1 + v2
    elif v3 == '-':
        return v1 - v2
    elif v3 == '*':
        return v1 * v2
    elif v3 == '/':
        return v1 / v2
    else:
        raise TypeError


def save_in_memory(result):
    answer = input(msg[4])
    if answer == 'y':
        if is_one_digit(result):
            global memory
            index = 10
            while index < 13 and answer == 'y':
                answer = input(msg[index])
                index += 1
                if index == 13:
                    memory = result
        else:
            memory = result
    elif answer != 'n':
        save_in_memory(result)


msg = [
    'Enter an equation\n',
    'Do you even know what numbers are? Stay focused!',
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    'Yeah... division by zero. Smart move...',
    'Do you want to store the result? (y / n):\n',
    'Do you want to continue calculations? (y / n):\n',
    ' ... lazy',
    ' ... very lazy',
    ' ... very, very lazy',
    'You are',
    'Are you sure? It is only one digit! (y / n)\n',
    "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
    'Last chance! Do you really want to embarrass yourself? (y / n)\n'
]

memory = None
calculator()
