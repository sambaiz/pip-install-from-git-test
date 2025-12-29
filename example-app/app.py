"""Example application using stats-lib and text-lib."""
from stats_lib import calculate_statistics
from text_lib import format_list


def main():
    # Calculate statistics
    numbers = [10, 20, 30, 40, 50]
    stats = calculate_statistics(numbers)

    print("Numbers:", format_list([str(n) for n in numbers]))
    print(f"Mean: {stats['mean']}")
    print(f"Median: {stats['median']}")
    print(f"Std: {stats['std']:.2f}")


if __name__ == "__main__":
    main()
