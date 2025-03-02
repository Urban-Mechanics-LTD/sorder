"""
sorder: A Python package for sorting and ordering operations.

This package provides utilities and tools for efficient sorting
and ordering of various data structures.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Import main classes for easy access
from sorder.core import Sorter, OrderManager
from sorder.utils import sort_helper, validate_input

# Define what's available when using `from sorder import *`
__all__ = ['Sorter', 'OrderManager', 'sort_helper', 'validate_input']

