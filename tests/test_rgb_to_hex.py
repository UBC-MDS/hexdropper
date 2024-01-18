import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.hexdropper.rgb_to_hex import rgb_to_hex

def test_standard_colors():
    assert rgb_to_hex(255, 0, 0) == '#FF0000'
    assert rgb_to_hex(0, 255, 0) == '#00FF00'
    assert rgb_to_hex(0, 0, 255) == '#0000FF'

def test_boundary_values():
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'

def test_specific_case():
    assert rgb_to_hex(76, 150, 29) == '#4C961D'

def test_edge_cases():
    assert rgb_to_hex(15, 15, 15) == '#0F0F0F'
    assert rgb_to_hex(16, 16, 16) == '#101010'

def test_tuple_input():
    assert rgb_to_hex((255, 0, 0)) == '#FF0000'
    assert rgb_to_hex((0, 255, 0)) == '#00FF00'
    assert rgb_to_hex((0, 0, 255)) == '#0000FF'

def run_tests():
    test_standard_colors()
    test_boundary_values()
    test_specific_case()
    test_edge_cases()
    test_tuple_input()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()