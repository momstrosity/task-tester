import pytest
from src.color_converter import rgb_to_hex

def test_rgb_to_hex_valid_inputs():
    """Test conversion of valid RGB values to hex."""
    assert rgb_to_hex(255, 255, 255) == "ffffff"
    assert rgb_to_hex(0, 0, 0) == "000000"
    assert rgb_to_hex(255, 0, 0) == "ff0000"
    assert rgb_to_hex(0, 255, 0) == "00ff00"
    assert rgb_to_hex(0, 0, 255) == "0000ff"
    assert rgb_to_hex(128, 128, 128) == "808080"

def test_rgb_to_hex_edge_cases():
    """Test edge cases of RGB conversion."""
    assert rgb_to_hex(0, 0, 0) == "000000"
    assert rgb_to_hex(255, 255, 255) == "ffffff"

def test_rgb_to_hex_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test out of range values
    with pytest.raises(ValueError, match="Red must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match="Green must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError, match="Blue must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)

def test_rgb_to_hex_wrong_type():
    """Test error handling for incorrect input types."""
    with pytest.raises(TypeError, match="Red must be an integer"):
        rgb_to_hex("255", 0, 0)
    with pytest.raises(TypeError, match="Green must be an integer"):
        rgb_to_hex(0, "255", 0)
    with pytest.raises(TypeError, match="Blue must be an integer"):
        rgb_to_hex(0, 0, "255")