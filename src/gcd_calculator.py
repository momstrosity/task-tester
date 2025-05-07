def prime_factors(n):
    """
    Calculate the prime factors of a given number.
    
    Args:
        n (int): The number to factorize.
    
    Returns:
        dict: A dictionary of prime factors with their exponents.
    """
    # Handle special cases
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Use absolute value to handle negative numbers
    n = abs(n)
    
    # Handle edge cases
    if n <= 1:
        return {} if n == 1 else {}
    
    factors = {}
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            # Count the number of times this prime factor appears
            count = 0
            while n % divisor == 0:
                n //= divisor
                count += 1
            factors[divisor] = count
        
        # Move to next potential prime divisor
        divisor += 1 if divisor == 2 else 2
    
    # If n is a prime number greater than 1
    if n > 1:
        factors[n] = 1
    
    return factors

def gcd(*numbers):
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        *numbers (int): Variable number of integers.
    
    Returns:
        int: The greatest common divisor of the input numbers.
    
    Raises:
        TypeError: If any input is not an integer.
        ValueError: If no arguments are provided.
    """
    # Validate inputs
    if len(numbers) == 0:
        raise ValueError("At least one number is required")
    
    # Convert to list and verify all are integers
    nums = list(numbers)
    
    # Handle single number case
    if len(nums) == 1:
        return abs(nums[0])
    
    # Get prime factorizations for all numbers
    all_factors = [prime_factors(num) for num in nums]
    
    # Find common prime factors with minimum exponents
    common_factors = {}
    for prime in set().union(*(f.keys() for f in all_factors)):
        # Find the minimum exponent of this prime across all numbers
        min_exponent = min(
            factor.get(prime, 0) for factor in all_factors
        )
        
        if min_exponent > 0:
            common_factors[prime] = min_exponent
    
    # Calculate GCD by multiplying common prime factors
    gcd_value = 1
    for prime, exponent in common_factors.items():
        gcd_value *= prime ** exponent
    
    return gcd_value