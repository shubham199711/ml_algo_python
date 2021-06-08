import numpy as np
# from __future__ import annotations


def relu(vector):
    return np.maximum(0, vector)


if __name__ == "__main__":
    # return max or 0 depending on value
    print(relu(np.array([-1, 23, 4, 4, 0, -32])))
