#!/usr/bin/env python3
import sys

from libs import templates
from libs.equation_model.equation_model import EquationModel
from libs.output.make_output_strings import create_reduced_form
from libs.parse.parse import parse
from libs.solve_equation.solve_degree_1 import solve_degree_1
from libs.solve_equation.solve_degree_2 import solve_degree_2


def get_args(equation_model: EquationModel) -> str:
    equation = None
    for arg in sys.argv:
        if '-' in arg and arg[1:].isalpha():
            if 's' in arg:
                equation_model.steps = True
            if 'f' in arg:
                equation_model.free_form = True
        if '=' in arg:
            equation = arg
    return equation


def main():
    equation_model = EquationModel()
    if equation := get_args(equation_model):
        if not parse(equation, equation_model):
            print(templates.TRASH_ERROR)
            return 1
        if int(equation_model.b) == 0 and int(equation_model.a) == 0 and int(equation_model.c) == 0:
            print("The solution is any real number!")
            return 0
        elif int(equation_model.b) == 0 and int(equation_model.a) == 0 and int(equation_model.c) != 0:
            print("There is no solution!")
            return 0
        print(templates.REDUCED_FORM.format(reduced_form=create_reduced_form(equation_model)))
        print(templates.POLYNOMIAL_DEGREE.format(degree=equation_model.degree))
        if equation_model.degree == 2:
            solve_degree_2(equation_model)
            if not equation_model.steps:
                if equation_model.x2 is None and equation_model.d == 0:
                    print(templates.D_EQUAL_0.format(x1=equation_model.x1))
                elif equation_model.d < 0:
                    print(templates.D_NEGATIVE.format(x1=equation_model.x1_s, x2=equation_model.x2_s))
                else:
                    print(templates.D_POSITIVE.format(x1=equation_model.x1, x2=equation_model.x2))
        elif equation_model.degree == 1:
            solve_degree_1(equation_model)
            if not equation_model.steps:
                print(templates.DEGREE_1_SOLUTION.format(x1=equation_model.x1))
        elif equation_model.degree > 2:
            print(templates.BIGGER_POLYNOMIAL_DEGREE_ERROR)
    else:
        print(templates.USAGE)
        return 0
    return 0


main()
