"""
Read numbers from the command line and calculate basic statistics.

Enter numbers one at a time. Type 'q' to finish.
The program reports the count, sum, mean, and sample variance.
"""


def read_values():
    """Read numeric values until the user enters 'q'."""
    values = []

    print("Enter values. Type 'q' when you are done.")

    while True:
        user_input = input("Value: ").strip()

        if user_input.lower() == "q":
            print("Input finished!")
            break

        try:
            values.append(float(user_input))
            print("Value added!")
        except ValueError:
            print("Please enter a valid number or 'q'.")

    return values


def calculate_statistics(values):
    """Return count, total, mean, and sample variance."""
    count = len(values)

    if count == 0:
        return count, 0, None, None

    total = sum(values)
    mean = total / count

    # Sample variance requires at least two observations.
    if count < 2:
        variance = None
    else:
        squared_deviations = sum((value - mean) ** 2 for value in values)
        variance = squared_deviations / (count - 1)

    return count, total, mean, variance


def main():
    values = read_values()
    count, total, mean, variance = calculate_statistics(values)

    print("Data:", values)
    print("n =", count)
    print("Total:", total)

    if mean is None:
        print("Mean: cannot be calculated because no values were entered.")
    else:
        print("Mean =", mean)

    if variance is None:
        print("Sample variance: requires at least two values.")
    else:
        print("Sample variance =", variance)


if __name__ == "__main__":
    main()
