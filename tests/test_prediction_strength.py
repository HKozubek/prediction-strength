from prediction_strength import prediction_strength
import numpy as np

def test_valid_prediction_strength():
    A = np.array([0, 0, 1, 1, 0])
    B = np.array([1, 0, 1, 1, 0])

    assert prediction_strength(A, B) == 1/3