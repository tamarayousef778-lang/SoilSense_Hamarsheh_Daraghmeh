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

def score_sample(self, sample):

    scores = {
        "ph_score": self._score_parameter(sample["ph"], 6.0, 7.5, 4.0, 9.0),

        "moisture_score": self._score_parameter(sample["moisture"], 40, 60, 10, 90),

        "nitrogen_score": self._score_parameter(sample["nitrogen"], 40, 80, 0, 120),

        "phosphorus_score": self._score_parameter(sample["phosphorus"], 20, 40, 0, 60),

        "potassium_score": self._score_parameter(sample["potassium"], 150, 250, 50, 350)
    }

    scores["total_score"] = round(sum(scores.values()), 1)

    return scores
def classify_sample(self, total_score):

    if total_score >= 90:
        return "Excellent"

    elif total_score >= 70:
        return "Good"

    elif total_score >= 50:
        return "Fair"

    else:
        return "Poor"