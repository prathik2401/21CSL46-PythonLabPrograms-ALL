def roman_to_decimal(roman):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    decimal = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_dict[numeral]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
            
        prev_value = value

    return decimal

# Test the function
roman_numeral = "XIV"  # Example: Roman numeral for 1994
decimal_value = roman_to_decimal(roman_numeral)
print(f"Decimal value: {decimal_value}")