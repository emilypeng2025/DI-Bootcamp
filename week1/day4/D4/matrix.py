import re

MATRIX_STRING = "7i3Tsih%xi #sM $a #t%^r!"
COLUMNS = 3
ROWS = 8

def build_matrix(string, columns):
    """Convert the string into a matrix with specified columns."""
    matrix = [char for char in string]
    return [list(row) for row in zip(*[iter(matrix)] * columns)]

def extract_no_digits(matrix, columns, rows):
    """Extract all characters that are NOT digits, column by column."""
    result = []
    for col in range(columns):
        for row in range(rows):
            if not matrix[row][col].isdigit():
                result.append(matrix[row][col])
    return "".join(result)

def clean_string(string, keep_exclamation=False):
    """Clean string by removing unwanted characters.
       Optionally keep exclamation mark.
       Also remove space before ! if found."""
    if keep_exclamation:
        pattern = '[^A-Za-z0-9!]+'
    else:
        pattern = '[^A-Za-z0-9]+'
        
    cleaned = re.sub(pattern, ' ', string)
    
    # Remove space before exclamation marks (e.g., ' !' -> '!')
    cleaned = re.sub(r'\s+!', '!', cleaned)
    
    return cleaned.strip()

# --- Main execution ---
matrix = build_matrix(MATRIX_STRING, COLUMNS)
print(matrix)

no_digits_string = extract_no_digits(matrix, COLUMNS, ROWS)

cleaned_string = clean_string(no_digits_string, keep_exclamation=True)
print(cleaned_string)