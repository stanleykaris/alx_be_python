def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats.
        num = float(numerator)
        den = float(denominator)
        # Attempt division operation
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
        
    except ValueError:
        return "Error: Please enter numeric values only."