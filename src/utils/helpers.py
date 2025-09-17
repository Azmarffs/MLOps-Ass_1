from typing import List


def normalize_list(values: List[float]) -> List[float]:
    if not values:
        return values
    min_v = min(values)
    max_v = max(values)
    if max_v == min_v:
        return [0.0 for _ in values]
    return [(v - min_v) / (max_v - min_v) for v in values]

