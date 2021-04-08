from libs.equation_model.equation_model import EquationModel


def solve_degree_1(model: EquationModel):
    model.x1 = round(-model.c / model.b, 4)
