from libs import templates
from libs.equation_model.equation_model import EquationModel


def show_steps(model: EquationModel):
    print(templates.STEPS_DEGREE_1.format(c=round(model.c, 4),
                                          b=round(model.b, 4),
                                          x1=round(model.x1, 4)))


def solve_degree_1(model: EquationModel):
    model.x1 = round(-model.c / model.b, 4)
    if model.steps:
        show_steps(model)
