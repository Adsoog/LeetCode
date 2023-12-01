def generate_pascals_triangle(numRows):
    if numRows == 0:
        return []
    
    # Initialize Pascal's Triangle with the first row
    triangle = [[1]]
    
    for _ in range(1, numRows):
        # Get the last row in the triangle
        last_row = triangle[-1]
        
        # Calculate the next row
        next_row = [1]
        for i in range(1, len(last_row)):
            next_row.append(last_row[i - 1] + last_row[i])
        next_row.append(1)
        
        # Append the next row to the triangle
        triangle.append(next_row)
    
    return triangle

# Example usage
numRows = 5
result = generate_pascals_triangle(numRows)
print(result)
