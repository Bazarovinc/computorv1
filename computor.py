import sys

from libs import templates
from libs.equation_model.equation_model import EquationModel
from libs.make_output_strings.utils import create_reduced_form
from libs.parse.parse import parse
from libs.solve_equation.solve_degree_1 import solve_degree_1
from libs.solve_equation.solve_degree_2 import solve_degree_2


def get_args(equation_model: EquationModel):
    equation = None
    for arg in sys.argv:
        if '-' in arg and 's' in arg:
            equation_model.steps = True
        elif '=' in arg:
            equation = arg
    return equation


def main():
    equation_model = EquationModel()
    if equation := get_args(equation_model):
        equation_model = parse(equation, equation_model)
        equation_model.make_degree()
        print(templates.REDUCED_FORM.format(reduced_form=create_reduced_form(equation_model)))
        print(templates.POLYNOMIAL_DEGREE.format(degree=equation_model.degree))
        if equation_model.degree == 2:
            solve_degree_2(equation_model)
            if not equation_model.steps:
                if equation_model.x2 is None and equation_model.d == 0:
                    print(templates.D_EQUAL_0.format(x1=equation_model.x1))
                elif equation_model.x1 and equation_model.x2 is None and equation_model.d < 0:
                    print(templates.D_NEGATIVE.format(x1=equation_model.x1, x2=equation_model.x2))
                else:
                    print(templates.D_POSITIVE.format(x1=equation_model.x1, x2=equation_model.x2))
        elif equation_model.degree == 1:
            solve_degree_1(equation_model)
            if not equation_model.steps:
                print(templates.DEGREE_1_SOLUTION.format(x1=equation_model.x1))
    else:
        print(templates.USAGE)
        return 1
    return 0


main()
