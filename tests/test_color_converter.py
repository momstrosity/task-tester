import pytest
from src.color_converter import rgb_to_hex

def test_standard_colors():
    """Test conversion of standard colors"""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(0, 0, 0) == '#000000'    # Black
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White

def test_mixed_colors():
    """Test conversion of mixed colors"""
    assert rgb_to_hex(128, 128, 128) == '#808080'  # Gray
    assert rgb_to_hex(255, 165, 0) == '#FFA500'   # Orange

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test out of range values
    with pytest.raises(ValueError, match="Red must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match="Green must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError, match="Blue must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)

def test_type_errors():
    """Test error handling for incorrect input types"""
    with pytest.raises(TypeError, match="Red must be an integer"):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError, match="Green must be an integer"):
        rgb_to_hex(0, '255', 0)
    with pytest.raises(TypeError, match="Blue must be an integer"):
        rgb_to_hex(0, 0, '255')