from libs.equation_model.equation_model import EquationModel
import re


def parse_polynomia_part(eq: str, degree: int):
    return re.findall(rf'[+]?[-]?\s?\d*[.]?\d*\s?[*]?\s?[X][^\\][{degree}]', eq)


def parse_nums(polynomial_part: list):
    num = 0
    sign = 1
    for part in polynomial_part:
        num_part = part.split('*')[0]
        sign_str = re.search(r'[+]?[-]?', num_part).group(0)
        if sign_str == '-':
            sign = -1
        elif sign_str == '+' or sign_str == '':
            sign = 1
        n = re.search(r'\d+[.]?\d+', num_part)
        if n is None:
            n = re.search(r'\d+', num_part)
        num += sign * float(n.group(0))
    return num


def parse_equation(eq: str, model: EquationModel, side: int):
    model.c += side * parse_nums(parse_polynomia_part(eq, 0))
    model.b += side * parse_nums(parse_polynomia_part(eq, 1))
    model.a += side * parse_nums(parse_polynomia_part(eq, 2))


def parse(equation: str, model: EquationModel):
    eq_1, eq_2 = equation.split('=')
    parse_equation(eq_1, model, 1)
    parse_equation(eq_2, model, -1)
    return model
