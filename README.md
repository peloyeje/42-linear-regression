# 42-linear-regression

The aim of this project is to implement from scratch a program that predicts the price of a car by using a linear function train with a gradient descent algorithm.

### Installation and usage

To train the algorithm:

```shell
$ pip install numpy
$ src/train.py -h
usage: train.py [-h] -i INPUT -m MODEL [-p]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The file containing the training data
  -m MODEL, --model MODEL
                        Output file to store the regressor
  -p, --plot            Print convergence and regression graphs
$ src/train.py -i data/data.csv -m data/model -p
```

To make predictions:

```shell
$ src/predict.py -h
usage: predict.py [-h] -m MODEL [-v VALUE]

optional arguments:
  -h, --help            show this help message and exit
  -m MODEL, --model MODEL
                        Trained model file
  -v VALUE, --value VALUE
                        Numerical mileage value to get price for
```

### Authors

- Sami Mhirech
- Jean-Eudes Peloye
- Guilhem Vuillier
