import matplotlib.pyplot as plt

class Visualizer:

    def nutrient_chart(self, sample):
        names = ["Nitrogen", "Phosphorus", "Potassium"]
        actual = [sample["nitrogen"], sample["phosphorus"], sample["potassium"]]
        ideal = [80, 40, 250]

        percentages = []

        for i in range(len(actual)):
            percent = (actual[i] / ideal[i]) * 100
            if percent > 150:
                percent = 150
            percentages.append(percent)

        colors = []

        for value in percentages:
            if value >= 100:
                colors.append("green")
            elif value >= 50:
                colors.append("orange")
            else:
                colors.append("red")

        plt.figure(figsize=(8, 5))
        plt.barh(names, percentages, color=colors)
        plt.axvline(x=100, color="black", linestyle="--")
        plt.xlabel("Percentage of ideal value")
        plt.title(f"Nutrient Levels — {sample['location']}")
        plt.xlim(0, 150)
        plt.tight_layout()
        plt.show()

    def ph_indicator(self, sample):
        fig, ax = plt.subplots(figsize=(10, 2))

        ax.axvspan(0, 6, color="red", alpha=0.4)
        ax.axvspan(6, 7.5, color="green", alpha=0.4)
        ax.axvspan(7.5, 14, color="orange", alpha=0.4)

        ax.axvline(x=sample["ph"], color="black", linewidth=3)

        ax.text(3, 0.5, "Acidic", ha="center")
        ax.text(6.75, 0.5, "Ideal", ha="center")
        ax.text(10.5, 0.5, "Alkaline", ha="center")

        ax.set_xlim(0, 14)
        ax.set_yticks([])
        ax.set_xlabel("pH value")
        ax.set_title(f"pH Indicator — {sample['location']} (pH = {sample['ph']})")

        plt.tight_layout()
        plt.show()

    def health_dashboard(self, results):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

        locations = []
        scores = []
        classes = []

        for sample in results:
            locations.append(sample["location"])
            scores.append(sample["total_score"])
            classes.append(sample["classification"])

        colors = []

        for score in scores:
            if score >= 90:
                colors.append("green")
            elif score >= 70:
                colors.append("blue")
            elif score >= 50:
                colors.append("orange")
            else:
                colors.append("red")

        ax1.bar(locations, scores, color=colors)
        ax1.set_ylim(0, 100)
        ax1.set_title("Soil Health Scores")
        ax1.set_ylabel("Score")

        for i in range(len(scores)):
            ax1.text(i, scores[i] + 2, f"{scores[i]}\n{classes[i]}", ha="center")

        ax1.tick_params(axis="x", rotation=35)

        counts = {}

        for c in classes:
            counts[c] = counts.get(c, 0) + 1

        labels = list(counts.keys())
        values = list(counts.values())

        pie_colors = []

        for label in labels:
            if label == "Excellent":
                pie_colors.append("green")
            elif label == "Good":
                pie_colors.append("blue")
            elif label == "Fair":
                pie_colors.append("orange")
            else:
                pie_colors.append("red")

        ax2.pie(values, labels=labels, colors=pie_colors, autopct="%1.1f%%")
        ax2.set_title("Classification Distribution")

        fig.suptitle("SoilSense — Smart Soil Analysis Dashboard")
        plt.tight_layout()
        plt.show()