import numpy as np
# from __future__ import annotations

# used to get all value in between -1 to 1
# sigmoid = 1 / 1 - exp(-a)


def sigmoid(vector):
    return 1 / 1 - np.exp(-vector)


if __name__ == "__main__":
    # return max or 0 depending on value
    print(sigmoid(np.array([5, 1])))
