import pytest
from src.color_converter import rgb_to_hex

def test_rgb_to_hex_valid_inputs():
    """Test conversion of valid RGB values to hex."""
    assert rgb_to_hex(255, 0, 0) == '#FF0000'  # Red
    assert rgb_to_hex(0, 255, 0) == '#00FF00'  # Green
    assert rgb_to_hex(0, 0, 255) == '#0000FF'  # Blue
    assert rgb_to_hex(128, 128, 128) == '#808080'  # Gray

def test_rgb_to_hex_edge_cases():
    """Test boundary values."""
    assert rgb_to_hex(0, 0, 0) == '#000000'  # Black
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'  # White

def test_rgb_to_hex_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Values outside 0-255 range
    with pytest.raises(ValueError, match="Red value must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    
    with pytest.raises(ValueError, match="Green value must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    
    with pytest.raises(ValueError, match="Blue value must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)

def test_rgb_to_hex_invalid_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Red value must be an integer"):
        rgb_to_hex('255', 0, 0)
    
    with pytest.raises(TypeError, match="Green value must be an integer"):
        rgb_to_hex(0, '255', 0)
    
    with pytest.raises(TypeError, match="Blue value must be an integer"):
        rgb_to_hex(0, 0, '255')