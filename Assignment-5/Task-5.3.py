from typing import Final, Dict
# Cache to store computed Fibonacci numbers (memoization)
_fib_cache: Dict[int, int] = {0: 0, 1: 1}


def fibonacci_recursive(n: int) -> int:
    """
    Return the n-th Fibonacci number using memoized recursion.

    Definition (0-indexed):
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n >= 2

    Uses memoization to avoid redundant calculations, making it efficient.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Check cache first
    if n in _fib_cache:
        return _fib_cache[n]
    
    # Compute and cache the result
    _fib_cache[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return _fib_cache[n]


if __name__ == "__main__":
    PROMPT: Final[str] = "Enter n (non-negative integer): "
    try:
        user_input = input(PROMPT).strip()
        n_value = int(user_input)
        # Print the Fibonacci series from F(0) to F(n) (space-separated)
        for i in range(n_value + 1):
            print(fibonacci_recursive(i), end=' ')
        print()
    except ValueError as exc:
        print(f"Invalid input: {exc}")
