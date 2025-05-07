import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    """Test prime numbers are correctly factorized."""
    assert prime_factorization(7) == [7]
    assert prime_factorization(17) == [17]
    assert prime_factorization(23) == [23]

def test_prime_factorization_edge_cases():
    """Test edge case scenarios."""
    assert prime_factorization(1) == []  # 1 has no prime factors
    assert prime_factorization(2) == [2]  # Smallest prime number

def test_prime_factorization_large_number():
    """Test factorization of a larger composite number."""
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_prime_factorization_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("12")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-5)

def test_prime_factorization_performance():
    """Verify factorization works with a moderately large number."""
    result = prime_factorization(123456)
    assert result == [2, 2, 2, 2, 2, 2, 3, 643]  # Corrected prime factors
    assert len(result) > 1  # Ensure multiple factors
    assert 2 ** 6 * 3 * 643 == 123456  # Verify the result reconstructs the original number