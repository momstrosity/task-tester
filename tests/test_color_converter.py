import pytest
from src.color_converter import rgb_to_hex

def test_basic_rgb_to_hex():
    """Test basic color conversion"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(0, 0, 0) == '#000000'    # Black
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White

def test_edge_cases():
    """Test boundary values"""
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'

def test_invalid_input_types():
    """Test type checking"""
    with pytest.raises(TypeError):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, '0', 0)
    with pytest.raises(TypeError):
        rgb_to_hex(255, 0, '0')

def test_out_of_range_values():
    """Test range validation"""
    with pytest.raises(ValueError):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError):
        rgb_to_hex(0, 0, 300)

def test_padding():
    """Test zero-padding for single-digit hex values"""
    assert rgb_to_hex(10, 15, 20) == '#0A0F14'