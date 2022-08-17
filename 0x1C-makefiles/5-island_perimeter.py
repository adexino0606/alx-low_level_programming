#!/usr/bin/python3
"""
define the function island_perimeter(grid):
that returns the perimeter of the island described in grid:
"""


def island_perimeter(grid):
    """
    Find the perimeter of a island
    (land and water is representated by 1 and 0 respectively)
    Args:
            - grid : int[][]
    """
    height = len(grid)
    width = len(grid[0])
    x, y, perimeter = 0, 0, 0

    for y in range(height):
        for x in range(width):
            if (grid[y][x] == 1):
                if (y - 1 < 0 or grid[y - 1][x] == 0):
                    perimeter += 1
                if (y + 1 == height or grid[y + 1][x] == 0):
                    perimeter += 1
                if (x - 1 < 0 or grid[y][x - 1] == 0):
                    perimeter += 1
                if (x + 1 == width or grid[y][x + 1] == 0):
                    perimeter += 1
    return (perimeter)
