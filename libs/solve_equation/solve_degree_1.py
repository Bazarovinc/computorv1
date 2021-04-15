from libs.equation_model.equation_model import EquationModel
from libs.output.write_output import write_steps_degree_1


def solve_degree_1(model: EquationModel):
    model.x1 = round(-model.c / model.b, 4)
    if model.steps:
        write_steps_degree_1(model)
