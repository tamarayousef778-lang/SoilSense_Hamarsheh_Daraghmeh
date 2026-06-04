import csv
import numpy as np
class SoilAnalyzer:
    pass
def load_samples(self, filepath):
    samples = []

    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                sample = {
                    "sample_id": int(row["sample_id"]),
                    "location": row["location"],
                    "ph": float(row["ph"]),
                    "moisture": float(row["moisture"]),
                    "nitrogen": float(row["nitrogen"]),
                    "phosphorus": float(row["phosphorus"]),
                    "potassium": float(row["potassium"])
                }

                samples.append(sample)

    except FileNotFoundError:
        raise FileNotFoundError("Soil data file not found")

    return samples
def _score_parameter(self, value, ideal_min, ideal_max, hard_min, hard_max):

    if ideal_min <= value <= ideal_max:
        return 20

    elif value < ideal_min:
        ratio = (value - hard_min) / (ideal_min - hard_min)

    else:
        ratio = (hard_max - value) / (hard_max - ideal_max)

    score = ratio * 20

    score = np.clip(score, 0, 20)

    return round(score, 1)