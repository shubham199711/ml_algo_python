import numpy as np
# from __future__ import annotations

# softmax = exp(a) / sum(exp(a))


def softmax(vector):
    exp_vec = np.exp(vector)
    exp_sum_vec = np.sum(exp_vec)
    return exp_vec / exp_sum_vec


if __name__ == "__main__":
    # return max or 0 depending on value
    print(softmax(np.array([5, 1])))
