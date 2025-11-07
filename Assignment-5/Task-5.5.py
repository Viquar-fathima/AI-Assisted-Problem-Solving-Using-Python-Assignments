def greet_user(name, gender):
    """
    Greet a user with an appropriate title based on their gender preference.
    Supports binary, non-binary, and gender-neutral options.
    
    Args:
        name: The user's name
        gender: Gender preference (male, female, non_binary, neutral, prefer_not_to_say, or any other value)
    
    Returns:
        A personalized greeting string
    """
    # Normalize gender input to lowercase for case-insensitive comparison
    gender_lower = gender.lower().strip()
    
    # Map gender preferences to appropriate titles
    if gender_lower == "male":
        title = "Mr."
    elif gender_lower in ["female", "woman"]:
        title = "Ms."
    elif gender_lower in ["non_binary", "non-binary", "nonbinary", "nb"]:
        title = "Mx."  # Gender-neutral title
    elif gender_lower in ["neutral", "gender-neutral"]:
        title = "Mx."  # Gender-neutral title
    elif gender_lower in ["prefer_not_to_say", "prefer not to say", "prefer_not_to_specify"]:
        # No title for those who prefer not to specify
        title = ""
    else:
        # Default: no title for unknown/invalid inputs (most inclusive approach)
        title = ""
    
    # Construct greeting
    if title:
        return f"Hello, {title} {name}! Welcome."
    else:
        return f"Hello, {name}! Welcome."


# Example usage and testing
if __name__ == "__main__":
    # Test cases demonstrating different gender options
    test_cases = [
        ("John", "male"),
        ("Sarah", "female"),
        ("Alex", "non_binary"),
        ("Taylor", "non-binary"),
        ("Jordan", "neutral"),
        ("Casey", "prefer_not_to_say"),
        ("Riley", "unknown"),  # Unknown input
        ("Morgan", ""),  # Empty string
    ]
    
    print("=== Gender-Inclusive Greeting System ===\n")
    for name, gender in test_cases:
        result = greet_user(name, gender)
        print(f"Input: name='{name}', gender='{gender}'")
        print(f"Output: {result}\n")
