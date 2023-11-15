tolerance_values = {"C": 1.5, "Si": 1, "S": 0.7}


def calculate_tolerance(element, min_rate, max_rate):
    tolerance = tolerance_values.get(element, None)
    relaxed_min, relaxed_max = None, None
    if tolerance:
        if min_rate is not None:
            relaxed_min = float(min_rate) * (1 - tolerance / 100)
        if max_rate is not None:
            relaxed_max = float(max_rate) * (1 + tolerance / 100)
    return relaxed_min, relaxed_max
