import csv
import numpy as np


class SoilAnalyzer:

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

        return round(float(score), 1)

    def score_sample(self, sample):

        scores = {
            "ph_score": self._score_parameter(
                sample["ph"], 6.0, 7.5, 4.0, 9.0
            ),

            "moisture_score": self._score_parameter(
                sample["moisture"], 40, 60, 10, 90
            ),

            "nitrogen_score": self._score_parameter(
                sample["nitrogen"], 40, 80, 0, 120
            ),

            "phosphorus_score": self._score_parameter(
                sample["phosphorus"], 20, 40, 0, 60
            ),

            "potassium_score": self._score_parameter(
                sample["potassium"], 150, 250, 50, 350
            )
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

    def get_recommendations(self, sample):

        recommendations = []

        if sample["ph"] < 6.0:
            recommendations.append(
                "Add agricultural lime to raise soil pH"
            )

        elif sample["ph"] > 7.5:
            recommendations.append(
                "Add elemental sulfur to lower soil pH"
            )

        if sample["moisture"] < 40:
            recommendations.append(
                "Increase irrigation frequency — soil is too dry"
            )

        elif sample["moisture"] > 60:
            recommendations.append(
                "Improve field drainage — soil is waterlogged"
            )

        if sample["nitrogen"] < 40:
            recommendations.append(
                "Apply nitrogen-rich fertilizer (e.g., urea or ammonium nitrate)"
            )

        if sample["phosphorus"] < 20:
            recommendations.append(
                "Apply phosphate fertilizer to support root development"
            )

        if sample["potassium"] < 150:
            recommendations.append(
                "Apply potassium fertilizer (e.g., potash) to improve disease resistance"
            )

        if len(recommendations) == 0:
            recommendations.append(
                "Soil is in ideal condition — no action needed"
            )

        return recommendations

    def analyze_all(self, samples):

        results = []

        for sample in samples:

            scores = self.score_sample(sample)

            result = sample.copy()

            result["scores"] = scores

            result["total_score"] = scores["total_score"]

            result["classification"] = self.classify_sample(
                scores["total_score"]
            )

            result["recommendations"] = self.get_recommendations(sample)

            results.append(result)

        all_scores = np.array(
            [sample["total_score"] for sample in results]
        )

        print(f"Class average score : {np.mean(all_scores):.1f}")
        print(f"Best sample score   : {np.max(all_scores):.1f}")
        print(f"Worst sample score  : {np.min(all_scores):.1f}")

        return results