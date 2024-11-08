def roman_to_integer(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    
    for i in range(len(s) - 1):
        # Check if current numeral is less than the next numeral
        if values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    
    # Add the value of the last numeral
    total += values[s[-1]]
    
    return total

# Test cases
print(roman_to_integer('I'))        # Expected output: 1
print(roman_to_integer('IX'))       # Expected output: 9
print(roman_to_integer('CDII'))     # Expected output: 402
print(roman_to_integer('MCMXCIV'))  # Expected output: 1994
print(roman_to_integer('MMXX'))     # Expected output: 2020