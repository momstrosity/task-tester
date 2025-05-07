import pytest
from src.gcd_calculator import prime_factors, gcd

def test_prime_factors():
    # Test simple cases
    assert prime_factors(12) == {2: 2, 3: 1}
    assert prime_factors(15) == {3: 1, 5: 1}
    
    # Test prime number
    assert prime_factors(17) == {17: 1}
    
    # Test 1 and edge cases
    assert prime_factors(1) == {}
    assert prime_factors(0) == {}
    
    # Test negative numbers
    assert prime_factors(-12) == {2: 2, 3: 1}

def test_prime_factors_error_handling():
    # Test non-integer input
    with pytest.raises(TypeError):
        prime_factors(3.14)
    
    with pytest.raises(TypeError):
        prime_factors("12")

def test_gcd():
    # Basic cases
    assert gcd(12, 15) == 3
    assert gcd(48, 18) == 6
    
    # Single number case
    assert gcd(17) == 17
    
    # Zero cases
    assert gcd(0, 5) == 5
    assert gcd(0, 0) == 0
    
    # Negative numbers
    assert gcd(-12, 15) == 3
    
    # Multiple numbers
    assert gcd(24, 36, 48) == 12

def test_gcd_error_handling():
    # No arguments
    with pytest.raises(ValueError):
        gcd()
    
    # Non-integer input
    with pytest.raises(TypeError):
        gcd(12, 3.14)
    
    with pytest.raises(TypeError):
        gcd("12", 15)