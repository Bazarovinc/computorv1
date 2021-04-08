from libs.equation_model.equation_model import EquationModel
from libs.math.ft_sqrt import ft_sqrt, ft_abs
from libs import templates


def show_steps(model: EquationModel):
    print(templates.STEPS_DEGREE_BEFORE_D.format(a=model.a,
                                                 b=model.b,
                                                 c=model.c,
                                                 b2=(model.b * model.b),
                                                 ac=(4 * model.a * model.c),
                                                 d=model.d))
    if model.d > 0:
        print(templates.STEPS_D_POSITIVE.format(a=model.a,
                                                b=model.b,
                                                sqrt_d=round(model.sqrt_d, 4),
                                                x1=model.x1,
                                                x2=model.x2,
                                                b_sqrt_d_1=round(-model.b - model.sqrt_d, 4),
                                                b_sqrt_d_2=round(-model.b + model.sqrt_d, 4),
                                                a2=round(2 * model.a, 4)))


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
        model.x1_s = f'{round(-model.b / 2 * model.a, 4)} - i{round(model.sqrt_d / 2 * model.a, 4)}'
        model.x2_s = f'{round(-model.b / 2 * model.a, 4)} + i{round(model.sqrt_d / 2 * model.a, 4)}'
    if model.steps:
        show_steps(model)
