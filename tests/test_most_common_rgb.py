import pytest
import numpy as np
from hexdropper.read_image import read_image
from hexdropper.most_common_rgb import most_common_rgb

# read in test data
arr1 = np.zeros((9, 10, 3)).astype(int)
arr2 = np.arange(255, 285).astype(int).reshape((1, 10, 3))
test_array1 = np.concatenate((arr2, arr1))

arr3 = np.zeros((9, 10, 3)).astype(float)
arr4 = np.arange((30)).astype(float).reshape((1, 10, 3))
test_array2 = np.concatenate((arr4, arr3))

test_array3 = test_array3 = np.random.randint(30, size=(10, 10, 4)).astype(int)

img_array = read_image('tests/images/cropped_img.jpg')

# Check input array values do not exceed 255
def test_input_array_values():
    with pytest.raises(ValueError):
        output = most_common_rgb(test_array1)
        
# check that values in the array are integers
def test_input_array_type():
    with pytest.raises(TypeError):
        output = most_common_rgb(test_array2)

# check that the input array's 3rd dimension is of size 3
def test_input_array_dim():
    with pytest.raises(ValueError):
        output = most_common_rgb(test_array3)
        
# check that the output matches the actual RGB value of the image
def test_most_common_rgb_output():
    assert most_common_rgb(img_array) == tuple([8, 181, 213])