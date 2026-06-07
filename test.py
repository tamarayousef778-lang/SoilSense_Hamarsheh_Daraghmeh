from soil_analyzer import SoilAnalyzer

analyzer = SoilAnalyzer()

samples = analyzer.load_samples("soil_readings.csv")

results = analyzer.analyze_all(samples)

for result in results:
    print(result["sample_id"])
    print(result["location"])
    print(result["total_score"])
    print(result["classification"])
    print(result["recommendations"])
    print()