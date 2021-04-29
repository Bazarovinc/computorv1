# computorv1
This project to solve polynomial equation of 1 and 2 degree.
## Start
* If you have Python3 on your PC run script `start.sh`
```
>./start.sh
```
* If you don't have Python3 on yout PC run script `start_wit_installation_mac.sh`
```
>./start_wit_installation_mac.sh
```
## Run project
To run project:
```
>./computor.py
```
You will get:
```
usage:
	./computor.py [-s] [equation]
		-s - the solutions will shown by steps
		-f - free form entrie
		equation - correct form should be: c * X^0 + b * X^1 + a * X^2 = 0, where a, b, c - is float
```
Put in argument equation like: "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
```
>./computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4.0 * X^0 + 4.0 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.9052
-0.4751
```
### Flags
* -s

The program will show you solving equation stat by step:
```
>./computor.py -s "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4.0 * X^0 + 4.0 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Solution stet by step:
	We got:
		a = -9.3
		b = 4.0
		c = 4.0
		a*X^2 + b*X + c = 0
		-9.3*X^2 + 4.0*X + 4.0 = 0
		D = b^2 - 4 * a * c = 4.0^2 - 4 * -9.3 * 4.0 = 16.0 - (-148.8) = 164.8
	Discriminant is strictly positive, the two solutions are:
		√D = 12.8374
		x1 = ( -b - √D) / (2 * a) = (-(4.0) - 12.8374) / (2 * -9.3) = -16.8374 / -18.6 = 0.9052
		x2 = ( -b + √D) / (2 * a) = (-(4.0) + 12.8374) / (2 * -9.3) = 8.8374 / -18.6 = -0.4751
```
* -f

You can put equation in free form, like:  "5 + 4 * X + X^2= X^2"
```
>./computor.py -f "5 + 4 * X + X^2= X^2"
Reduced form: 5.0 * X^0 + 4.0 * X^1 = 0
Polynomial degree: 1
The solution is:
-1.25
```
