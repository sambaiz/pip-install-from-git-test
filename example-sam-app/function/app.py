"""Lambda function using stats-lib and text-lib."""
from stats_lib import calculate_statistics
from text_lib import format_list


def handler(event, context):
    """Lambda handler function."""
    numbers = [10, 20, 30, 40, 50]
    stats = calculate_statistics(numbers)

    result = {
        "numbers": format_list([str(n) for n in numbers]),
        "mean": stats['mean'],
        "median": stats['median'],
        "std": round(stats['std'], 2)
    }

    return {
        "statusCode": 200,
        "body": result
    }
