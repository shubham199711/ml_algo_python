from numpy.random import rand
from numpy import arange, asarray
import matplotlib.pyplot as plt


def derivative(x):
    return x * 2.0


def objective(x):
    return x**2.0


def gradient_descent(n_iter, step_size, bounds, derivative, objective):
    # generate initial point
    solution = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    solutions, scores = [], []
    for i in range(n_iter):
        gradient = derivative(solution)
        solution = solution - step_size * gradient
        solution_eval = objective(solution)
        solutions.append(solution)
        scores.append(solution_eval)
        # print('>%d f(%s) = %.5f' % (i, solution, solution_eval))
    return [solutions, scores]


if __name__ == "__main__":
    bounds = asarray([[-1.0, 1.0]])
    solutions, scores = gradient_descent(
        30, 0.1, bounds, derivative, objective)
    inputs = arange(bounds[0, 0], bounds[0, 1]+0.1, 0.1)
    results = objective(inputs)
    plt.plot(inputs, results)
    plt.plot(solutions, scores, '.-', color='red')
    plt.show()
