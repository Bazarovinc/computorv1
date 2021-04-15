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
    if model.degree >= 2:
        if model.a < 0:
            reduced_form += f'- {-1 * model.a} * X^2 '
        elif model.a >= 0:
            reduced_form += f'+ {model.a} * X^2 '
    if model.degree > 2:
        for polynomial_part in reversed(model.other_degrees):
            if polynomial_part.degree <= model.degree:
                if polynomial_part.coefficient < 0:
                    reduced_form += f'- {-1 * polynomial_part.coefficient} * X^{polynomial_part.degree} '
                elif model.a >= 0:
                    reduced_form += f'+ {polynomial_part.coefficient} * X^{polynomial_part.degree} '
    reduced_form += '= 0'
    return reduced_form