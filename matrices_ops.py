import sys
import numpy as np

def setup_matrices():
    first_grid = np.arange(1, 5).reshape(2, 2)
    second_grid = np.arange(6, 10).reshape(2, 2)
    return first_grid, second_grid

def add_elements(grid1, grid2):
    return grid1 + grid2

def multiply_elements(grid1, grid2):
    return grid1 * grid2

def dot_product(grid1, grid2):
    return grid1 @ grid2

def show_output(first_grid, second_grid):
    print("=" * 50)
    print("2x2 ARRAY OPERATIONS")
    print("=" * 50)
    
    print(f"\nArray A:\n{first_grid}")
    print(f"\nArray B:\n{second_grid}")
    
    print("\n" + "-" * 30)
    print("OPERATIONS:")
    print("-" * 30)
    
    sum_grid = add_elements(first_grid, second_grid)
    print(f"\nElement-wise Addition (A + B):\n{sum_grid}")
    
    product_grid = multiply_elements(first_grid, second_grid)
    print(f"\nElement-wise Multiplication (A * B):\n{product_grid}")
    
    dot_result = dot_product(first_grid, second_grid)
    print(f"\nMatrix Multiplication (A @ B):\n{dot_result}")
    
    print("\n" + "=" * 50)

def check_dimensions(first_grid, second_grid):
    
    if first_grid.shape != second_grid.shape:
        print(f"Error: Array shapes don't match. A: {first_grid.shape}, B: {second_grid.shape}")
        return False
    
    if first_grid.shape != (2, 2):
        print(f"Error: Expected 2x2 arrays, got {first_grid.shape}")
        return False
    
    return True

def main():
   
    try:
       
        first_grid, second_grid = setup_matrices()
        
      
        if not check_dimensions(first_grid, second_grid):
            return 1
        
        show_output(first_grid, second_grid)
        
        return 0
        
    except Exception as error:
        print(f"An error occurred: {error}")
        return 1

if __name__ == "__main__":
    sys.exit(main())