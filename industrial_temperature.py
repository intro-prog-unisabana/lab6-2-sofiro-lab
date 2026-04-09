def trigger_alarm(temperatures, threshold=80):
    result = []

    for sensor, temp in temperatures.items():
        if temp > threshold:  # estrictamente mayor
            result.append(sensor)

    return result