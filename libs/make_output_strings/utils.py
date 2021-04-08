from libs.equation_model.equation_model import EquationModel


def create_reduced_form(model: EquationModel) -> str:
    reduced_form = ''
    if model.c < 0:
        reduced_form += f'- {-1 * model.c} * X^0 '
    elif model.c >= 0:
        reduced_form += f'{model.c} * X^0 '
    if model.b < 0:
        reduced_form += f'- {-1 * model.b} * X^1 '
    elif model.b >= 0:
        reduced_form += f'+ {model.b} * X^1 '
    if model.a < 0:
        reduced_form += f'- {-1 * model.a} * X^2 '
    elif model.a >= 0:
        reduced_form += f'+ {model.a} * X^2 '
    reduced_form += '= 0'
    return reduced_form
