"""Statistical utility functions."""
import numpy as np
from typing import List, Dict, Union


def calculate_statistics(numbers: List[Union[int, float]]) -> Dict[str, float]:
    """
    Calculate basic statistics for a list of numbers.

    Args:
        numbers: A list of numbers (int or float)

    Returns:
        A dictionary containing:
            - mean: The average value
            - median: The median value
            - std: The standard deviation
            - min: The minimum value
            - max: The maximum value

    Raises:
        ValueError: If the input list is empty

    Example:
        >>> calculate_statistics([1, 2, 3, 4, 5])
        {'mean': 3.0, 'median': 3.0, 'std': 1.414..., 'min': 1.0, 'max': 5.0}
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")

    arr = np.array(numbers)

    return {
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "std": float(np.std(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
    }
