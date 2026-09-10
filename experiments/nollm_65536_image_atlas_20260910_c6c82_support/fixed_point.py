Q16_ONE = 65536
WEIGHT_FORMAT = "q16_65536"


def normalize_q16_weights(raw_weights: list[int]) -> tuple[int, ...]:
    if not raw_weights or any(type(value) is not int or value < 0 for value in raw_weights) or sum(raw_weights) <= 0:
        raise ValueError("weights must be non-negative integers with positive total")
    total = sum(raw_weights)
    result = [(value * Q16_ONE) // total for value in raw_weights]
    order = sorted(range(len(raw_weights)), key=lambda index: (-((raw_weights[index] * Q16_ONE) % total), index))
    for index in order[: Q16_ONE - sum(result)]:
        result[index] += 1
    return tuple(result)
