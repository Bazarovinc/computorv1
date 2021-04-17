import re
from typing import Tuple, Optional, List

from libs.equation_model.equation_model import EquationModel, OtherDegrees


def parse_polynomial_part(eq: str, degree: int) -> list:
    return re.findall(rf'[+]?[-]?\s?\d*[.]?\d*\s?[*]?\s?[X][^\\][{degree}]', eq)


def parse_nums(polynomial_part: list, eq_string: str) -> Tuple[float, str]:
    num: float = 0
    sign = 1
    for part in polynomial_part:
        if not part:
            continue
        eq_string = eq_string.replace(part, '')
        if '*' in part:
            num_part = part.split('*')[0]
        else:
            num_part = part
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


def parse_free_form_equation(eq: str, model: EquationModel, side: int) -> str:
    a, eq = parse_nums(parse_polynomial_part(eq, 2), eq)
    eq = eq.strip()
    model.a += side * a
    b, eq = parse_nums(re.findall(r'[+]?[-]?\s?\d*[.]?\d*\s?[*]?\s?[X]', eq), eq)
    eq = eq.strip()
    model.b += side * b
    c, eq = parse_nums(re.findall(r'[+]?[-]?\s?\d*[.]?\d*', eq), eq)
    eq = eq.strip()
    model.c += side * c
    return eq


def parse_other_degrees(eq: str, side: int) -> Tuple[str, Optional[List[OtherDegrees]]]:
    other_degrees = []
    for i in reversed(range(3, 5)):
        coef, eq = parse_nums(parse_polynomial_part(eq, i), eq)
        if int(coef) != 0:
            other_degrees.append(OtherDegrees(coefficient=side * coef, degree=i))
    if len(other_degrees) == 0:
        return eq, None
    return eq, other_degrees


def check_others_degrees(eq_1: str, eq_2: str, model: EquationModel) -> Tuple[str, str]:
    if 'X' in eq_1:
        eq_1, model.other_degrees = parse_other_degrees(eq_1, 1)
    if 'X' in eq_2:
        if model.other_degrees is None:
            eq_2, model.other_degrees = parse_other_degrees(eq_2, -1)
        else:
            j = 0
            for i in range(3, model.degree):
                coef, eq_1 = parse_nums(parse_polynomial_part(eq_2, i), eq_2)
                if int(coef) != 0:
                    model.other_degrees[j].coefficient -= coef
                j += 1
    return eq_1, eq_2


def find_max_degree(eq, model):
    degrees = re.findall(r'[X][^\\]?\d*', eq)
    for degree in degrees:
        degree_num = re.search(r'\d+', degree)
        if degree_num is None:
            continue
        if int(degree_num.group(0)) > model.degree:
            model.degree = int(degree_num.group(0))


def parse(equation: str, model: EquationModel):
    find_max_degree(equation, model)
    eq_1, eq_2 = equation.split(' = ')
    if eq_2 == '0':
        eq_2 = ''
    if model.degree > 2:
        eq_1, eq_2 = check_others_degrees(eq_1, eq_2, model)
        eq_1, eq_2 = eq_1.strip(), eq_2.strip()
    if model.free_form:
        eq_1 = parse_free_form_equation(eq_1, model, 1).strip()
        eq_2 = parse_free_form_equation(eq_2, model, 1).strip()
    else:
        eq_1 = parse_equation(eq_1, model, 1).strip()
        eq_2 = parse_equation(eq_2, model, -1).strip()
    if model.other_degrees is None:
        model.set_degree()
    if not eq_1 and not eq_2:
        return True
    return False
