from termcolor import colored

REDUCED_FORM = "Reduced form: {reduced_form}"
POLYNOMIAL_DEGREE = "Polynomial degree: {degree}"
D_POSITIVE = "Discriminant is strictly positive, the two solutions are:\n{x1}\n{x2}"
D_EQUAL_0 = "Discriminant is equal to 0, the solution is:\n{x1}"
D_NEGATIVE = "Discriminant is negative, the two solutions are:\n{x1}\n{x2}"
DEGREE_1_SOLUTION = "The solution is:\n{x1}"
USAGE = 'usage:\n' \
        '\t./computor [-s] [equation]\n' \
        '\t\t-s - the solutions will shown by steps\n' \
        '\t\tequation - correct form should be: c * X^0 + b * X^1 + a * X^2 = 0, where a, b, c - is float'
STEPS_DEGREE_2_BEFORE_D = \
    "Solution stet by step:\n\tWe got:\n\t\t" + colored("a = {a}\n\t\t", 'red') + colored("b = {b}\n\t\t", 'blue') + \
    colored("c = {c}\n\t\t", 'yellow') + colored("D", 'cyan') + " = " + colored("b", 'blue') + "^2 - 4 * " +\
    colored("a", 'red') + " * " + colored("c", 'yellow') + " = " + colored("{b}", 'blue') + "^2 - 4 * " +\
    colored("{a}", 'red') + " * " + colored("{c}", 'yellow') + " = {b2} - ({ac}) = " + colored("{d}", 'cyan')
STEPS_D_POSITIVE = \
    colored("\tDiscriminant", 'cyan') + " is strictly " +\
    colored("positive", 'green', attrs=['underline']) + ", the two solutions are:\n\t\t" + \
    colored("√D = {sqrt_d}\n\t\t", 'magenta') + colored("x1", 'green', attrs=['reverse']) + " = ( -" +\
    colored("b", 'blue') + " - " + colored("√D", 'magenta') + ") / 2 * " + colored("a", 'red') + " = (-(" +\
    colored("{b}", 'blue') + ") - " + colored("{sqrt_d}", 'magenta') + ") / 2 * " + colored("{a}", 'red') +\
    " = {b_sqrt_d_1} / {a2} = " + colored("{x1}", 'green', attrs=['reverse']) + "\n\t\t" + \
    colored("x2", 'yellow', attrs=['reverse']) + " = ( -" + colored("b", 'blue') + " + " + colored("√D", 'magenta') +\
    ") / 2 * " + colored("a", 'red') + " = (-(" + colored("{b}", 'blue') + ") - " + colored("{sqrt_d}", 'magenta') +\
    ") / 2 * " + colored("{a}", 'red') + " = {b_sqrt_d_2} / {a2} = " + colored("{x2}", 'yellow', attrs=['reverse'])
STEPS_D_NEGATIVE = \
    colored("\tDiscriminant", 'cyan') + " is strictly " +\
    colored("negative", 'red', attrs=['underline']) + ", the two solutions are:\n\t\t" + \
    colored("√|D| = {sqrt_d}\n\t\t", 'magenta') + colored("x1", 'green', attrs=['reverse']) + " = ( -" +\
    colored("b", 'blue') + " - i" + colored("√|D|", 'magenta') + ") / 2 * " + colored("a", 'red') + " = (-(" +\
    colored("{b}", 'blue') + ") - i" + colored("{sqrt_d}", 'magenta') + ") / 2 * " + colored("{a}", 'red') + " = " +\
    colored("{x1}", 'green', attrs=['reverse']) + "\n\t\t" + colored("x2", 'yellow', attrs=['reverse']) +\
    " = ( -" + colored("b", 'blue') + " + i" + colored("√|D|", 'magenta') +\
    ") / 2 * " + colored("a", 'red') + " = (-(" + colored("{b}", 'blue') + ") - i" + colored("{sqrt_d}", 'magenta') +\
    ") / 2 * " + colored("{a}", 'red') + " = " + colored("{x2}", 'yellow', attrs=['reverse'])
STEPS_D_EQ_0 = \
    colored("\tDiscriminant", 'cyan') + " is equal " + \
    colored("0", 'blue', attrs=['underline']) + ", the solution is:\n\t\t" + colored('x', 'green', attrs=['reverse']) +\
    " = -" + colored("b", 'blue') + " / 2 * " + colored("a", 'red') + " = -" + colored("{b}", 'blue') + " / 2 * " +\
    colored("{a}", 'red') + " = " + colored("{x1}", 'green', attrs=['reverse'])
STEPS_DEGREE_1 = \
    "Solution stet by step:\n\tWe got:\n\t\t" + colored("c = {c}\n\t\t", 'red') + colored("b = {b}\n\t\t", 'blue') + \
    "Solution is:\n\t\t" + colored("x", 'green') + " = -" + colored("c", 'red') + " / " + colored("b", 'blue') + \
    " = -(" + colored("{c}", 'red') + ") / " + colored("{b}", 'blue') + " = " + colored("{x1}", 'green')
TRASH_ERROR = colored("Error!", 'red') + "\nSome trash in equation!"
BIGGER_POLYNOMIAL_DEGREE_ERROR = "The polynomial degree is strictly greater than 2, I can't solve."
