from termcolor import colored
REDUCED_FORM = "Reduced form: {reduced_form}"
POLYNOMIAL_DEGREE = "Polynomial degree: {degree}"
D_POSITIVE = "Discriminant is strictly positive, the two solutions are:\n{x1}\n{x2}"
D_EQUAL_0 = "Discriminant is equal to 0, the solution is:\n{x1}"
D_NEGATIVE = "Discriminant is negative, the two solutions are:\n{x1}\n{x2}"
DEGREE_1_SOLUTION = "The solution is:\n{x1}"
USAGE = 'usage:\n' \
        './computor [-s] [equation]\n' \
        '-s - the solutions will show by steps\n' \
        'equation - correct form should be: c * X^0 + b * X^1 + a * X^2 = 0, where a, b, c - is float'
STEPS_DEGREE_BEFORE_D = \
    "Solution stet by step:\nWe got:\n" + colored("a = {a}\n", 'red') + colored("b = {b}\n", 'blue') + \
    colored("c = {c}\n", 'yellow') + colored("D", 'cyan') + " = " + colored("b", 'blue') + "^2 - 4 * " +\
    colored("a", 'red') + " * " + colored("c", 'yellow') + " = " + colored("{b}", 'blue') + "^2 - 4 * " +\
    colored("{a}", 'red') + " * " + colored("{c}", 'yellow') + " = {b2} - ({ac}) = " + colored("{d}", 'cyan') + " " +\
    colored("> 0", 'green', attrs=['underline'])
STEPS_D_POSITIVE = \
    colored("Discriminant", 'cyan') + " is strictly " +\
    colored("positive", 'green', attrs=['underline']) + ", the two solutions are:\n" + \
    colored("√D = {sqrt_d}\n", 'magenta') + colored("x1", 'green', attrs=['reverse']) + " = ( -" +\
    colored("b", 'blue') + " - " + colored("√D", 'magenta') + ") / 2 * " + colored("a", 'red') + " = (-(" +\
    colored("{b}", 'blue') + ") - " + colored("{sqrt_d}", 'magenta') + ") / 2 * " + colored("{a}", 'red') +\
    " = {b_sqrt_d_1} / {a2} = " + colored("{x1}", 'green', attrs=['reverse']) + "\n" + \
    colored("x2", 'yellow', attrs=['reverse']) + " = (- " + colored("b", 'blue') + " + " + colored("√D", 'magenta') +\
    ") / 2 * " + colored("a", 'red') + " = (-(" + colored("{b}", 'blue') + ") - " + colored("{sqrt_d}", 'magenta') +\
    ") / 2 * " + colored("{a}", 'red') + " = {b_sqrt_d_2} / {a2} = " + colored("{x2}", 'yellow', attrs=['reverse'])
