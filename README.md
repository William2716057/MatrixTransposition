# MatrixTransposition

This Python code performs matrix transposition on a given matrix to rearrange the horizontal columns vertically. It swaps the rows and columns of the input matrix to create a transposed matrix.

## Code Description

The code takes an input matrix 'A' and transposes it to generate a new matrix 'TranspositionResult', where the rows of the original matrix become columns in the transposed matrix.

### Input Matrix 'A'

A = [[5, 4, 3],
     [2, 4, 6],
     [4, 7, 9],
     [8, 1, 4]]

How It Works

1. An empty matrix TranspositionResult is initialized with zeros and dimensions reversed compared to the original matrix A.

2. Nested loops iterate over the elements of the original matrix A. The outer loop iterates over rows, and the inner loop iterates over columns.

3. The value at row a and column b in matrix A is assigned to the position at row b and column a in the transposed matrix TranspositionResult. This effectively swaps the positions of elements from the original matrix to achieve the transposition.

4. After the transposition is complete, the transposed matrix is printed.

Usage
Replace the content of the A matrix with your desired values to perform transposition on a different matrix.

Run the script.
