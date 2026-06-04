import csv

def create_sample_data(filepath="soil_readings.csv"):
    samples = [
        ["sample_id", "location", "ph", "moisture", "nitrogen", "phosphorus", "potassium"],
        [1, "Field A - North", 6.5, 50, 60, 30, 200],
        [2, "Field B - South", 5.1, 28, 18, 8, 85],
        [3, "Field C - East", 7.9, 65, 85, 50, 290],
        [4, "Greenhouse 1", 6.8, 55, 55, 25, 190],
        [5, "Greenhouse 2", 4.5, 20, 10, 5, 60],
        [6, "Field D - West", 7.2, 45, 45, 35, 220],
    ]

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(samples)

    print(f"Sample data created: {filepath}")

if __name__ == "__main__":
    create_sample_data()