from libs import templates
from libs.equation_model.equation_model import EquationModel
from libs.output.make_output_strings import create_colored_equation


def write_steps_degree_1(model: EquationModel):
    print(templates.STEPS_DEGREE_1_GOT.format(c=round(model.c, 4),
                                              b=round(model.b, 4)))
    print(create_colored_equation(model))
    print(templates.STEPS_SOLUTION_DEGREE_1.format(c=round(model.c, 4),
                                                   b=round(model.b, 4),
                                                   x1=round(model.x1, 4)))


def write_steps_degree_2(model: EquationModel):
    print(templates.STEPS_DEGREE_2_GOT.format(a=model.a,
                                              b=model.b,
                                              c=model.c))
    print(create_colored_equation(model))
    print(templates.STEPS_D.format(a=model.a,
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
    elif model.d < 0:
        print(templates.STEPS_D_NEGATIVE.format(a=model.a,
                                                b=model.b,
                                                sqrt_d=round(model.sqrt_d, 4),
                                                x1=model.x1_s,
                                                x2=model.x2_s,
                                                b_sqrt_d_1=round(-model.b - model.sqrt_d, 4),
                                                b_sqrt_d_2=round(-model.b + model.sqrt_d, 4),
                                                a2=round(2 * model.a, 4)))
    elif model.d == 0:
        print(templates.STEPS_D_EQ_0.format(a=model.a,
                                            b=model.b,
                                            x1=model.x1,
                                            a2=round(2 * model.a, 4)))
