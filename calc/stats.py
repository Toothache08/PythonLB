def calculate_stats(numbers):
    if not numbers:
        raise ValueError("Числовой ряд пуст")

    count = len(numbers)
    total = sum(numbers)
    mean = total / count
    sum_squares = sum(x * x for x in numbers)
    rms = (sum_squares / count) ** 0.5
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = variance ** 0.5

    # Стандартное отклонение выборки
    sample_std_dev = (
        (sum((x - mean) ** 2 for x in numbers) / (count - 1)) ** 0.5
        if count > 1 else None
    )

    minimum = min(numbers)
    maximum = max(numbers)
    positive_count = sum(1 for x in numbers if x > 0)
    negative_count = sum(1 for x in numbers if x < 0)

    return {
        "count": count,
        "sum": total,
        "mean": mean,
        "sum_squares": sum_squares,
        "rms": rms,
        "variance": variance,
        "std_dev": std_dev,
        "sample_std_dev": sample_std_dev,
        "min": minimum,
        "max": maximum,
        "positive_count": positive_count,
        "negative_count": negative_count,
    }
    