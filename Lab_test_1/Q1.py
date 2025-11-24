def fibonacci(n: int) -> list[int]:
    """
    Generate the Fibonacci sequence up to n terms.

    Parameters:
    n (int): Number of terms (must be positive).

    Returns:
    list[int]: Fibonacci sequence of length n.

    Raises:
    ValueError: If n is not a positive integer.
    """
    if n <= 0:
        raise ValueError("Number of terms must be a positive integer.")

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]


# --- Interactive part ---
def main():
    try:
        user_input = int(input("Enter the number of terms for Fibonacci sequence: "))
        result = fibonacci(user_input)
        print(f"Fibonacci sequence with {user_input} terms: {result}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")

if __name__ == "__main__":
    main()
