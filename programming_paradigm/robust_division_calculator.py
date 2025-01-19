def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats.
        num = float(numerator)
        den = float(denominator)
        # Attempt division operation
        result = num / den
        return result
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None
    