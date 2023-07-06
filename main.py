import math, sys

def calculator(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "abs": abs,
            "pi": math.pi,
            "e": math.e
        })
        return result
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        return "Error: Incorrect expression"

expression = sys.argv[1]
result = calculator(expression)
print("Result:", result)
