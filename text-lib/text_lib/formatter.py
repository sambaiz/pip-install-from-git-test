"""Text formatting utilities."""
from typing import List


def format_list(items: List[str], separator: str = ", ") -> str:
    """
    Format a list of strings into a single formatted string.

    Args:
        items: List of strings to format
        separator: String to use between items (default: ", ")

    Returns:
        Formatted string

    Example:
        >>> format_list(["apple", "banana", "cherry"])
        'apple, banana, cherry'
    """
    return separator.join(items)
