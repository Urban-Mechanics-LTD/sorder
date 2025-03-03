"""
Utility functions for the sorder package.

This module provides helper functions and utilities that are used
across the package for common tasks.
"""

def sort_helper(data, reverse=False):
    """
    A helper function for sorting data.
    
    Args:
        data: The data to be sorted
        reverse (bool): Whether to sort in reverse order
                    (default: False)
                    
    Returns:
        The sorted data
    """
    # Placeholder for actual implementation
    return sorted(data, reverse=reverse)


def validate_input(data):
    """
    Validate that input data is sortable.
    
    Args:
        data: The data to be validated
        
    Returns:
        bool: True if data is valid, False otherwise
    """
    # Placeholder for actual implementation
    try:
        iter(data)
        return True
    except TypeError:
        return False


def benchmark_sort(data, algorithms=None):
    """
    Benchmark different sorting algorithms on the provided data.
    
    Args:
        data: The data to benchmark with
        algorithms (list): List of algorithm names to benchmark
        
    Returns:
        dict: Performance metrics for each algorithm
    """
    # Placeholder for actual implementation
    return {"quick": 0.001, "merge": 0.002}

