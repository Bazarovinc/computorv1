from libs.equation_model.equation_model import EquationModel
from libs.math.ft_sqrt import ft_abs, ft_sqrt
from libs.output.write_output import write_steps_degree_2


def solve_degree_2(model: EquationModel):
    model.d = (model.b * model.b) - (4 * model.a * model.c)
    if model.d == 0:
        model.x1 = (-model.b) / (2 * model.a)
    elif model.d > 0:
        model.sqrt_d = ft_sqrt(model.d)
        model.x1 = round((-model.b - model.sqrt_d) / (2 * model.a), 4)
        model.x2 = round((-model.b + model.sqrt_d) / (2 * model.a), 4)
    elif model.d < 0:
        model.sqrt_d = ft_sqrt(ft_abs(model.d))
        model.x1_s = f'{round((-model.b / (2 * model.a)), 4)} - i{round(model.sqrt_d / (2 * model.a), 4)}'
        model.x2_s = f'{round((-model.b / (2 * model.a)), 4)} + i{round(model.sqrt_d / (2 * model.a), 4)}'
    if model.steps:
        write_steps_degree_2(model)
