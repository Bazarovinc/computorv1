import re
from typing import Tuple

from libs.equation_model.equation_model import EquationModel, OtherDegrees


def parse_polynomial_part(eq: str, degree: int) -> list:
    return re.findall(rf'[+]?[-]?\s?\d*[.]?\d*\s?[*]?\s?[X][^\\][{degree}]', eq)


def parse_nums(polynomial_part: list, eq_string: str) -> Tuple[float, str]:
    num: float = 0
    sign = 1
    for part in polynomial_part:
        eq_string = eq_string.replace(part, '')
        num_part = part.split('*')[0]
        if 'X' in num_part:
            num += 1
        else:
            sign_str = re.search(r'[+]?[-]?', num_part).group(0)
            if sign_str == '-':
                sign = -1
            elif sign_str == '+' or sign_str == '':
                sign = 1
            n = re.search(r'\d+[.]?\d+', num_part)
            if n is None:
                n = re.search(r'\d+', num_part)
            num += sign * float(n.group(0))
    return num, eq_string


def parse_equation(eq: str, model: EquationModel, side: int) -> str:
    c, eq = parse_nums(parse_polynomial_part(eq, 0), eq)
    model.c += side * c
    b, eq = parse_nums(parse_polynomial_part(eq, 1), eq)
    model.b += side * b
    a, eq = parse_nums(parse_polynomial_part(eq, 2), eq)
    model.a += side * a
    return eq


def parse_other_degrees(eq: str, side: int) -> Tuple[str, list]:
    other_degrees = []
    for i in reversed(range(3, 11)):
        coef, eq = parse_nums(parse_polynomial_part(eq, i), eq)
        other_degrees.append(OtherDegrees(coefficient=side * coef, degree=i))
    return eq, other_degrees


def check_others_degrees(eq_1: str, eq_2: str, model: EquationModel) -> Tuple[str, str]:
    if 'X' in eq_1:
        eq_1, model.other_degrees = parse_other_degrees(eq_1, 1)
    if 'X' in eq_2:
        if model.other_degrees is None:
            eq_2, model.other_degrees = parse_other_degrees(eq_2, -1)
        else:
            j = 0
            for i in reversed(range(3, 11)):
                coef, eq_1 = parse_nums(parse_polynomial_part(eq_2, i), eq_2)
                model.other_degrees[j].coefficient -= coef
                j += 1
    return eq_1, eq_2


def parse(equation: str, model: EquationModel):
    eq_1, eq_2 = equation.split(' = ')
    eq_1 = parse_equation(eq_1, model, 1).replace(' ', '')
    eq_2 = parse_equation(eq_2, model, -1).replace(' ', '')
    if eq_1 == '' and eq_2 == '':
        return True
    else:
        eq_1, eq_2 = check_others_degrees(eq_1, eq_2, model)
    if not eq_1 and not eq_2:
        return True
    return False
