import pytest
from src.color_converter import rgb_to_hex

def test_basic_rgb_to_hex_conversion():
    """Test standard RGB to Hex conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(0, 0, 0) == '#000000'   # Black
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White

def test_edge_case_conversions():
    """Test edge case RGB values"""
    assert rgb_to_hex(128, 128, 128) == '#808080'  # Mid-Gray
    assert rgb_to_hex(1, 1, 1) == '#010101'       # Near Black
    assert rgb_to_hex(254, 254, 254) == '#FEFEFE'  # Near White

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, [0], 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, 0, None)

def test_out_of_range_values():
    """Test error handling for out-of-range RGB values"""
    with pytest.raises(ValueError):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 0, 300)