import pytest
import os
from PIL import Image
from hexdropper.create_color_image import create_color_image

# Test data
valid_hex_code = '#FF5733'
invalid_hex_code = '#ZZZ999'
valid_image_size = (200, 200)
invalid_image_size = 'invalid_size'
output_path = os.path.join('tests', 'output', 'test_image.png')

# Test function with valid inputs
def test_create_color_image_valid():
    create_color_image(valid_hex_code, valid_image_size, output_path)
    assert os.path.isfile(output_path)
    os.remove(output_path)

# Test function with invalid hex code
def test_create_color_image_invalid_hex():
    with pytest.raises(ValueError):
        create_color_image(invalid_hex_code, valid_image_size, output_path)

# Test function with invalid image size
def test_create_color_image_invalid_size():
    with pytest.raises(ValueError):
        create_color_image(valid_hex_code, invalid_image_size, output_path)

# Test function without specifying output path
def test_create_color_image_no_output_path():
    create_color_image(valid_hex_code, valid_image_size)
    default_output_path = valid_hex_code.lstrip('#') + '.png'
    assert os.path.isfile(default_output_path)
    os.remove(default_output_path)
