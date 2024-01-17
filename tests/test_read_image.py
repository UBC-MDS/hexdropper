import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.hexdropper.read_image import read_image

# Test data
filepath_cropped_image_jpg = "tests\\images\\cropped_image.jpg"
filepath_uncropped_image_png = "tests\\images\\uncropped_image.png"
empty_filepath = ""
invalid_filepath = "C:\not\a\file"

# Test for correct return type on png image
def test_read_image_returns_array():
    assert isinstance(read_image(filepath_uncropped_image_png), np.ndarray)

# Test for correct return type on jpg image
def test_read_image_returns_array():
    assert isinstance(read_image(filepath_cropped_image_jpg), np.ndarray)

# Test returned array has RGB value for each pixel
def test_correct_output_dim():
    assert read_image(filepath_cropped_image_jpg).shape[2] == 3

# Test error is thrown for empty file path
def test_error_empty_path():
    with pytest.raises(ValueError):
        img = read_image(empty_filepath)

# Test error is thrown for invalid file path
def test_error_invalid_path():
    with pytest.raises(ValueError):
        img = read_image(invalid_filepath)