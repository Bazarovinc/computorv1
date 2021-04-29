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
./computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4.0 * X^0 + 4.0 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.9052
-0.4751
```
