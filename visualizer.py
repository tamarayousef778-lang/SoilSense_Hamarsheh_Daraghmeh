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
        plt.show()

sample = {

    "location": "Gaza",

    "nitrogen": 60,

    "phosphorus": 30,

    "potassium": 200

}

v = Visualizer()

v.nutrient_chart(sample)
